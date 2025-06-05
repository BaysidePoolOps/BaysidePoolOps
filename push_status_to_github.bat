@echo off
cd /d S:\PoolRepo\BaysidePoolOps
git add status.json
git commit -m "Update status"
git push
pause