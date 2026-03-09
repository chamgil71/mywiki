import os
import shutil
import re
import yaml

OBSIDIAN_PATH = r"C:\obsidian"
QUARTZ_CONTENT = r"C:\ai\mywiki\content"

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


def convert_links(text):

    # [[note]]
    text = re.sub(r"\[\[([^\]]+)\]\]", r"[\1](\1.md)", text)

    # ![[image.png]]
    text = re.sub(r"!\[\[([^\]]+)\]\]", r"![](\1)", text)

    return text


def export_notes():

    if not os.path.exists(QUARTZ_CONTENT):
        os.makedirs(QUARTZ_CONTENT)

    # 기존 content 삭제
    for f in os.listdir(QUARTZ_CONTENT):
        path = os.path.join(QUARTZ_CONTENT, f)

        if os.path.isfile(path):
            os.remove(path)

    # obsidian 스캔
    for root, dirs, files in os.walk(OBSIDIAN_PATH):

        for file in files:

            if not file.endswith(".md"):
                continue

            src = os.path.join(root, file)

            if not is_publish_true(src):
                continue

            with open(src, "r", encoding="utf-8") as f:
                text = f.read()

            text = convert_links(text)

            dst = os.path.join(QUARTZ_CONTENT, file)

            with open(dst, "w", encoding="utf-8") as f:
                f.write(text)

            print("export:", file)


if __name__ == "__main__":
    export_notes()