import os, re, sys, shutil, hashlib
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv

load_dotenv()

# ── 1. 환경 설정 ─────────────────────────────────────────────────────────────
OBSIDIAN_PATH = Path(os.getenv("OBSIDIAN_PATH"))
CONTENT_PATH  = Path(os.getenv("CONTENT_PATH"))
IMAGE_DIR     = CONTENT_PATH / os.getenv("IMAGE_DIR", "assets/image")
DOC_DIR       = CONTENT_PATH / os.getenv("DOC_DIR", "assets/docs")

# 설정된 배포 폴더를 경로가 긴 순서대로 정렬 (a/b/c가 a/b보다 우선순위를 가짐)
PUBLISH_FOLDERS = sorted(
    [Path(p.strip()) for p in os.getenv("PUBLISH_FOLDERS", "").split(",") if p.strip()],
    key=lambda x: len(x.parts), reverse=True
)

# 파일명 충돌 및 이미지 매핑 관리
image_map = {} # {original_name: final_name}

# ── 2. 유틸리티 함수 ──────────────────────────────────────────────────────────

def get_file_hash(path):
    """파일의 MD5 해시값을 반환 (대용량 대응 분할 읽기)"""
    h = hashlib.md5()
    with open(path, "rb") as f:
        while chunk := f.read(8192): h.update(chunk)
    return h.hexdigest()

def is_publish_true(path):
    """노트 상단 20줄 내에 publish: true가 있는지 확인"""
    try:
        with open(path, encoding="utf-8") as f:
            head = "".join([next(f) for _ in range(20)])
            return "publish: true" in head.lower()
    except: return False

def get_smart_dest_path(src_file):
    """사용자 규칙에 따른 목적지 경로 계산 (a/b/c 지정 시 content/c/...)"""
    for p_folder in PUBLISH_FOLDERS:
        try:
            # 파일이 지정된 폴더 하위인지 확인 (중복 시 구체적 경로 우선)
            src_file.relative_to(OBSIDIAN_PATH / p_folder)
            # 기준점의 부모를 통해 폴더명(c)부터 경로 유지
            return CONTENT_PATH / p_folder.name / src_file.relative_to(OBSIDIAN_PATH / p_folder)
        except ValueError: continue
    # 지정 폴더 외의 publish 파일은 루트로 보냄
    return CONTENT_PATH / src_file.name

def get_unique_path(target_path, src_file):
    """파일명 중복 시 상위 폴더명 또는 해시를 prefix로 붙여 고유 경로 생성"""
    if not target_path.exists(): return target_path
    
    # 1단계: 상위 폴더명 접두어 (예: 기술도서_개요.md)
    prefix = src_file.parent.name
    new_path = target_path.parent / f"{prefix}_{target_path.name}"
    
    # 2단계: 여전히 중복이면 해시 4자리 접두어 (예: a7f2_개요.md)
    if new_path.exists():
        h = get_file_hash(src_file)[:4]
        new_path = target_path.parent / f"{h}_{target_path.name}"
    
    return new_path

# ── 3. 에셋(이미지/문서) 처리 ──────────────────────────────────────────────────

def sync_asset(name):
    """내용이 변한 파일만 복사하는 증분 업데이트 방식"""
    # 옵시디언 전체에서 파일 탐색
    src = None
    for root, _, files in os.walk(OBSIDIAN_PATH):
        if name in files:
            src = Path(root) / name
            break
    if not src: return name

    ext = src.suffix.lower()
    target_base = IMAGE_DIR if ext in {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'} else DOC_DIR
    target_base.mkdir(parents=True, exist_ok=True)
    
    h = get_file_hash(src)
    dst = target_base / name

    # 이름은 같으나 내용이 다른 경우 해시 Prefix 부여
    if dst.exists() and get_file_hash(dst) != h:
        dst = target_base / f"{h[:4]}_{name}"

    # 변경된 경우에만 물리적 복사 수행 (용량/시간 절약)
    if not dst.exists():
        shutil.copy2(src, dst)
    
    return dst.name

def process_content(text):
    """이미지/문서 링크를 최적화된 경로로 치환"""
    def repl(m):
        raw_name = m.group(1).split("|")[0].strip()
        filename = os.path.basename(raw_name)
        # 에셋 동기화 및 최종 파일명 획득
        final_name = sync_asset(filename)
        return f"![{final_name}](/assets/image/{final_name})"

    # 위키링크 ![[이미지]] 및 마크다운 ![](이미지) 모두 대응
    text = re.sub(r"!\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", repl, text)
    text = re.sub(r"!\[[^\]]*\]\(([^)]+)\)", repl, text)
    
    # 일반 위키링크 [[링크]] -> [링크](/파일명) 변환
    text = re.sub(r"\[\[([^\]]+)\]\]", 
                  lambda m: f"[{m.group(1).split('|')[-1]}](/{os.path.basename(m.group(1).split('|')[0])})", 
                  text)
    return text

# ── 4. 메인 배포 로직 ──────────────────────────────────────────────────────────

def export_all():
    print(f"🚀 배포 시작: {datetime.now().strftime('%H:%M:%S')}")
    
    # [중요] 에셋은 보존하고 마크다운 문서만 삭제하여 속도 최적화
    if CONTENT_PATH.exists():
        for md in CONTENT_PATH.rglob("*.md"): md.unlink()
    
    # 필수 폴더 강제 생성
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    DOC_DIR.mkdir(parents=True, exist_ok=True)

    # 전체 스캔
    for r, _, files in os.walk(OBSIDIAN_PATH):
        for f in files:
            if not f.endswith(".md"): continue
            src_file = Path(r) / f
            
            if is_publish_true(src_file):
                # 1. 경로 결정 및 중복 방지 명명
                dst_file = get_smart_dest_path(src_file)
                dst_file = get_unique_path(dst_file, src_file)
                
                # 2. 내용 처리 (링크 치환 및 에셋 복사 포함)
                content = process_content(src_file.read_text(encoding="utf-8"))
                
                # 3. 파일 쓰기
                dst_file.parent.mkdir(parents=True, exist_ok=True)
                dst_file.write_text(content, encoding="utf-8")
                print(f"📄 {src_file.name} -> {dst_file.relative_to(CONTENT_PATH)}")

    # static_pages/ 폴더가 있으면 content/에 덮어씌움
    static_pages = Path(__file__).parent / "static_pages"
    if static_pages.exists():
        for src in static_pages.rglob("*"):
            if src.is_file():
                dst = CONTENT_PATH / src.relative_to(static_pages)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                print(f"📌 static: {src.name}")

if __name__ == "__main__":
    export_all()
    print(f"✨ 완료: {datetime.now().strftime('%H:%M:%S')}")