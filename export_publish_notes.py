import os
import shutil
import yaml
import subprocess
import sys
from dotenv import load_dotenv

load_dotenv()

OBSIDIAN_PATH = os.getenv("OBSIDIAN_PATH")
QUARTZ_CONTENT = os.getenv("CONTENT_PATH")
QUARTZ_PATH = os.path.dirname(QUARTZ_CONTENT)

# 예: PUBLISH_FOLDERS=msshin/60-AI/기술도서작성,msshin/50-DEV
PUBLISH_FOLDERS = [
    f.strip().replace("/", os.sep)
    for f in os.getenv("PUBLISH_FOLDERS", "").split(",")
    if f.strip()
]

USAGE = """
사용법: python export_publish_notes.py [명령]

  export   - Obsidian에서 publish:true 파일만 content로 복사
  push     - git add / commit / push
  all      - export + push 한번에
  dry-run  - 복사 없이 대상 파일 목록만 출력
"""


def is_publish_true(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        if not text.startswith("---"):
            return False
        frontmatter = text.split("---")[1]
        data = yaml.safe_load(frontmatter)
        return data.get("publish", False) == True
    except:
        return False


def get_scan_roots():
    """항상 OBSIDIAN_PATH 전체 스캔"""
    return [OBSIDIAN_PATH]


def get_dst_path(src):
    """
    src 경로에서 content 내 목적지 경로 계산.
    PUBLISH_FOLDERS 기준 폴더의 마지막 폴더명부터 구조 유지.

    예) OBSIDIAN_PATH/msshin/60-AI/기술도서작성/옵시디언가이드/a.md
        → content/기술도서작성/옵시디언가이드/a.md
    """
    for folder in PUBLISH_FOLDERS:
        scan_root = os.path.join(OBSIDIAN_PATH, folder)
        if src.startswith(scan_root):
            top = os.path.basename(scan_root)       # 기술도서작성
            rel = os.path.relpath(src, scan_root)   # 옵시디언가이드/a.md
            return os.path.join(QUARTZ_CONTENT, top, rel)

    # PUBLISH_FOLDERS 에 없는 파일: content/ 루트에 flat하게
    return os.path.join(QUARTZ_CONTENT, os.path.basename(src))


def collect_targets():
    """publish:true 인 md 파일 목록 반환 [(src, dst), ...]"""
    targets = []
    for scan_root in get_scan_roots():
        for root, dirs, files in os.walk(scan_root):
            for file in files:
                if not file.endswith(".md"):
                    continue
                src = os.path.join(root, file)
                if is_publish_true(src):
                    dst = get_dst_path(src)
                    targets.append((src, dst))
    return targets


def clean_content():
    """index.md 제외하고 content 폴더 초기화"""
    for f in os.listdir(QUARTZ_CONTENT):
        if f == "index.md":
            continue
        path = os.path.join(QUARTZ_CONTENT, f)
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)


def cmd_export():
    if not os.path.exists(QUARTZ_CONTENT):
        os.makedirs(QUARTZ_CONTENT)
    clean_content()

    targets = collect_targets()
    for src, dst in targets:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"  [export] {os.path.relpath(dst, QUARTZ_CONTENT)}")

    print(f"\n완료: {len(targets)}개 export")
    return len(targets)


def cmd_push(count=None):
    msg = f"update: {count} notes" if count else "update notes"
    print("\ngit push 중...")
    subprocess.run(["git", "-C", QUARTZ_PATH, "add", "."])
    subprocess.run(["git", "-C", QUARTZ_PATH, "commit", "-m", msg])
    subprocess.run(["git", "-C", QUARTZ_PATH, "push"])
    print("push 완료!")


def cmd_all():
    count = cmd_export()
    cmd_push(count)


def cmd_dry_run():
    targets = collect_targets()
    print("\n[dry-run] 복사 대상 파일 목록:")
    for src, dst in targets:
        print(f"  {os.path.relpath(dst, QUARTZ_CONTENT)}")
        print(f"    ← {src}")
    print(f"\n총 {len(targets)}개 (실제 복사 안 함)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(USAGE)
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "export":
        cmd_export()
    elif cmd == "push":
        cmd_push()
    elif cmd == "all":
        cmd_all()
    elif cmd == "dry-run":
        cmd_dry_run()
    else:
        print(f"알 수 없는 명령: {cmd}")
        print(USAGE)
        sys.exit(1)