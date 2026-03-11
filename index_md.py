from pathlib import Path
import datetime

content = Path("content")
lines = ["# Wiki Index\n", f"> Last Updated: {datetime.datetime.now():%Y-%m-%d %H:%M}\n"]

# 파일명 순 정렬
md_files = sorted(content.rglob("*.md"), key=lambda x: x.name)

for md in md_files:
    if md.name == "index.md": continue
    
    rel_path = md.relative_to(content).with_suffix('').as_posix()
    # 생성일 정보 가져오기
    c_time = datetime.datetime.fromtimestamp(md.stat().st_ctime)
    
    lines.append(f"- [[{rel_path}]] — _{c_time:%Y-%m-%d}_")

(content / "index.md").write_text("\n".join(lines), encoding="utf-8")