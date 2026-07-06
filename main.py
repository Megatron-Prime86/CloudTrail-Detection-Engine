import json
from detections import detect

with open("sample_logs.json") as file:
    logs = json.load(file)

print("\nCloudTrail Detection Report\n")

for event in logs:

    result = detect(event)

    print(
        f"User: {event['Username']} | "
        f"Event: {event['EventName']}"
    )

    if result:
        print("Alert:", result)

    print("-" * 40)