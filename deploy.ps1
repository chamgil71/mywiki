

C:\coding\.venv\Scripts\Activate.ps1


cd C:\quartz\mywiki

C:\coding\.venv\Scripts\Activate.ps1

python export_publish_notes.py

npx quartz build

git add .

git commit -m "update site"

git push