@echo off
set /p userpass=Enter PIN to CLOSED Aquatic: 
if NOT "%userpass%"=="8080" (
    echo Incorrect PIN. Action canceled.
    pause
    exit /b
)
set /p confirm=Are you sure you want to set Aquatic to CLOSED? (y/n): 
if /i NOT "%confirm%"=="y" (
    echo Action canceled.
    pause
    exit /b
)
python S:\StreamDeck\update_pool_status_shared.py aquatic closed
pause
