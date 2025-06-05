@echo off
cd /d S:\PoolRepo\BaysidePoolOps
python update_pool_status_shared.py kayaks closed
call "S:\PoolRepo\BaysidePoolOps\push_status_to_github.bat"
