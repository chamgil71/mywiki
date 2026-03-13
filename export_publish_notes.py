import os
import re
import sys
import shutil
import hashlib
import subprocess
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv

load_dotenv()

# ---------------------------
# 환경 설정
# ---------------------------

OBSIDIAN_PATH = Path(os.getenv("OBSIDIAN_PATH"))
CONTENT_PATH = Path(os.getenv("CONTENT_PATH"))
IMAGE_DIR = CONTENT_PATH / os.getenv("IMAGE_DIR", "assets/image")
DOC_DIR = CONTENT_PATH / os.getenv("DOC_DIR", "assets/docs")

IMAGE_EXT = {
    "." + x.strip().lower().lstrip(".")
    for x in os.getenv("IMAGE_EXT", "").split(",")
    if x.strip()
}

DOC_EXT = {
    "." + x.strip().lower().lstrip(".")
    for x in os.getenv("DOC_EXT", "").split(",")
    if x.strip()
}

PUBLISH_FOLDERS = [
    p.strip() for p in os.getenv("PUBLISH_FOLDERS", "").split(",") if p.strip()
]

# ---------------------------
# 정규식
# ---------------------------

WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
IMAGE_WIKI = re.compile(r"!\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
IMAGE_MD = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


# ---------------------------
# 유틸
# ---------------------------

def file_hash(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def is_publish_true(path):
    try:
        with open(path, encoding="utf-8") as f:
            head = "".join([next(f) for _ in range(20)])
    except:
        return False

    return "publish: true" in head.lower()


# ---------------------------
# 링크 변환
# ---------------------------

def convert_wikilinks(text):

    def repl(match):

        content = match.group(1)

        if content.startswith("!"):
            return match.group(0)

        if "|" in content:
            target, label = content.split("|", 1)
        else:
            target = label = content

        target = target.split("#")[0]

        return f"[{label}](/{target})"

    return WIKILINK.sub(repl, text)


# ---------------------------
# asset 수집
# ---------------------------

def collect_assets(text):

    assets = set()

    for m in IMAGE_WIKI.findall(text):
        assets.add(m.strip())

    for m in IMAGE_MD.findall(text):
        assets.add(m.strip())

    return assets


# ---------------------------
# asset 찾기
# ---------------------------

def find_asset(name):

    for root, dirs, files in os.walk(OBSIDIAN_PATH):
        if name in files:
            return Path(root) / name

    return None


# ---------------------------
# 노트 export
# ---------------------------

def export_note(src, dst, dry=False):

    with open(src, encoding="utf-8") as f:
        text = f.read()

    text = convert_wikilinks(text)

    assets = collect_assets(text)

    if not dry:
        dst.parent.mkdir(parents=True, exist_ok=True)

        with open(dst, "w", encoding="utf-8") as f:
            f.write(text)

    return assets


# ---------------------------
# asset 복사
# ---------------------------

def copy_asset(name, dry=False):

    src = find_asset(name)

    if not src:
        return None

    ext = src.suffix.lower()

    if ext in IMAGE_EXT:
        dst = IMAGE_DIR / name
    elif ext in DOC_EXT:
        dst = DOC_DIR / name
    else:
        return None

    if dst.exists():
        if file_hash(src) == file_hash(dst):
            return dst

    if not dry:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    return dst


# ---------------------------
# publish 노트 수집
# ---------------------------

def get_scan_roots():
    return [OBSIDIAN_PATH / f for f in PUBLISH_FOLDERS]


def collect_notes():

    notes = []

    for root in get_scan_roots():

        for r, d, files in os.walk(root):

            for f in files:

                if not f.endswith(".md"):
                    continue

                src = Path(r) / f

                if is_publish_true(src):

                    rel = src.relative_to(root)

                    dst = CONTENT_PATH / root.name / rel

                    notes.append((src, dst))

    return notes


# ---------------------------
# unused asset 정리
# ---------------------------

def cleanup_unused_assets():

    used = set()

    for md in CONTENT_PATH.rglob("*.md"):
        txt = md.read_text(encoding="utf-8")
        used |= collect_assets(txt)

    for folder in [IMAGE_DIR, DOC_DIR]:

        if not folder.exists():
            continue

        for f in folder.glob("*"):

            if f.name not in used:
                f.unlink()


# ---------------------------
# export 전체
# ---------------------------

def export_all(dry=False):

    notes = collect_notes()

    all_assets = set()

    for src, dst in notes:

        print("NOTE:", src)

        assets = export_note(src, dst, dry)

        all_assets |= assets

    print("assets:", len(all_assets))

    with ThreadPoolExecutor() as exe:
        exe.map(lambda a: copy_asset(a, dry), all_assets)

    if not dry:
        cleanup_unused_assets()


# ---------------------------
# git push
# ---------------------------

def git_push():

    date = datetime.now().strftime("%Y-%m-%d")

    msg = f"notes.py 자동생성 - {date}"

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", msg])
    subprocess.run(["git", "push"])


# ---------------------------
# main
# ---------------------------

def main():

    if len(sys.argv) < 2:
        print("사용법: python export_publish_notes.py [명령]")
        print("")
        print("  export   - publish:true 노트 export")
        print("  push     - git push")
        print("  all      - export + push")
        print("  dry-run  - 복사 없이 대상만 출력")
        return

    cmd = sys.argv[1]

    if cmd == "export":
        export_all()

    elif cmd == "dry-run":
        export_all(dry=True)

    elif cmd == "push":
        git_push()

    elif cmd == "all":
        export_all()
        git_push()


if __name__ == "__main__":
    main()