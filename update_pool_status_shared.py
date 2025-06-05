import json
import sys
from datetime import datetime

STATUS_FILE = "status.json"
LOG_FILE = "status_log.txt"

VALID_FACILITIES = {
    "sun_ridge": "Sun Ridge Pool",
    "commons": "Commons Pool",
    "point": "The Point Pool",
    "aquatic": "Aquatic Club",
    "kayaks": "Kayaks"
}

def log_change(facility_key, status, method="Manual override"):
    now = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    facility_name = VALID_FACILITIES.get(facility_key, facility_key)
    log_entry = f"{now} {facility_name} set to {status.upper()} ({method})"
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry + "\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python update_pool_status_shared.py [facility] [open|closed]")
        return

    facility = sys.argv[1].lower()
    status = sys.argv[2].lower()

    if facility not in VALID_FACILITIES:
        print("Invalid facility name.")
        return

    if status not in ("open", "closed"):
        print("Invalid status. Use 'open' or 'closed'.")
        return

    try:
        with open(STATUS_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {k: "closed" for k in VALID_FACILITIES}

    previous_status = data.get(facility)
    data[facility] = status

    with open(STATUS_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"{facility} set to {status}")
    if previous_status != status:
        log_change(facility, status)

if __name__ == "__main__":
    main()
