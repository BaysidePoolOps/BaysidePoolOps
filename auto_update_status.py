import json
from datetime import datetime

STATUS_FILE = "status.json"

# Time-based status logic
now = datetime.utcnow()
hour = now.hour

if hour == 14:  # 10 AM ET (UTC+4)
    pool_status = "open"
elif hour == 23:  # 7 PM ET (UTC+4)
    pool_status = "closed"
else:
    pool_status = None

if hour == 12:  # 8 AM ET (UTC+4)
    kayak_status = "open"
elif hour == 19:  # 3 PM ET (UTC+4)
    kayak_status = "closed"
else:
    kayak_status = None

# Load existing or initialize
try:
    with open(STATUS_FILE, "r") as f:
        status_data = json.load(f)
except FileNotFoundError:
    status_data = {
        "sun_ridge": "closed",
        "commons": "closed",
        "point": "closed",
        "aquatic": "closed",
        "kayaks": "closed"
    }

# Apply updates
if pool_status:
    for key in ["sun_ridge", "commons", "point", "aquatic"]:
        status_data[key] = pool_status

if kayak_status:
    status_data["kayaks"] = kayak_status

# Write safely
with open(STATUS_FILE, "w") as f:
    json.dump(status_data, f, indent=2)

print("Updated status:", status_data)
