@echo off
set /p userpass=Enter PIN to CLOSED Commons: 
if NOT "%userpass%"=="8080" (
    echo Incorrect PIN. Action canceled.
    pause
    exit /b
)
set /p confirm=Are you sure you want to set Commons to CLOSED? (y/n): 
if /i NOT "%confirm%"=="y" (
    echo Action canceled.
    pause
    exit /b
)
python S:\StreamDeck\update_pool_status_shared.py commons closed
pause
