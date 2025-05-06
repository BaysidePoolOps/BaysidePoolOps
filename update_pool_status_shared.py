
import json
import sys

POOL_FILE = "S:/StreamDeck/status.json"  # Shared network drive path

pool = sys.argv[1].lower()
status = sys.argv[2].lower()

with open(POOL_FILE, 'r') as f:
    data = json.load(f)

if pool in data:
    data[pool] = status
else:
    print("Invalid pool name.")
    sys.exit(1)

with open(POOL_FILE, 'w') as f:
    json.dump(data, f)

print(f"{pool} set to {status}")
