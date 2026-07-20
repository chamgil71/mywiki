
# deploy.ps1 - Obsidian → Quartz → GitHub Pages 배포

# 1. 가상환경 활성화
C:\ai\.venv\Scripts\Activate.ps1

# 2. Quartz 프로젝트 폴더로 이동
Set-Location -Path C:\ai\mywiki

# 3. Obsidian 노트 export (git push는 스크립트 안에서 처리)
python export_publish_notes.py all
