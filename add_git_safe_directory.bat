@echo off
echo Adding Git safe.directory for shared repo access...
git config --global --add safe.directory "//cmfc-utilities/StreamDeck/PoolRepo/BaysidePoolOps"
echo Done. This user can now use Git in the shared PoolRepo folder.
pause
