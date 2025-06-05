@echo off
echo Setting up Git Credential Manager and safe directory...

:: Set the safe Git directory to avoid ownership errors
git config --global --add safe.directory "//cmfc-utilities/StreamDeck/PoolRepo/BaysidePoolOps"

:: Set Git to use Windows Credential Manager
git config --global credential.credentialStore wincredman

:: Trigger a GitHub login prompt (only runs if in the correct repo)
cd /d "//cmfc-utilities/StreamDeck/PoolRepo/BaysidePoolOps"
git pull

echo Setup complete. GitHub login (if prompted) should now be saved.
pause
