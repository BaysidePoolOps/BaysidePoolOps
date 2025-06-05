@echo off
set /p confirm=Are you sure you want to set Sun Ridge to CLOSED? (y/n):
if /i NOT "%confirm%"=="y" (
    echo Action canceled.
    pause
    exit /b
)
cd /d S:\PoolRepo\BaysidePoolOps
python update_pool_status_shared.py sun_ridge closed
call "S:\PoolRepo\BaysidePoolOps\push_status_to_github.bat"
