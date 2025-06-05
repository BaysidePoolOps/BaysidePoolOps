@echo off
set /p confirm=Are you sure you want to set Commons to CLOSED? (y/n):
if /i NOT "%confirm%"=="y" (
    echo Action canceled.
    pause
    exit /b
)
cd /d S:\PoolRepo\BaysidePoolOps
python update_pool_status_shared.py commons closed
call "S:\PoolRepo\BaysidePoolOps\push_status_to_github.bat"
