@echo off
set /p confirm=Are you sure you want to set Point to OPEN? (y/n):
if /i NOT "%confirm%"=="y" (
    echo Action canceled.
    pause
    exit /b
)
cd /d S:\PoolRepo\BaysidePoolOps
python update_pool_status_shared.py point open
call "S:\PoolRepo\BaysidePoolOps\push_status_to_github.bat"
