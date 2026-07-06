from mitre_mapping import MITRE_MAP
from risk_score import calculate_risk
from incident_summary import generate_summary

logs = [
    {"EventName": "ConsoleLogin", "Username": "subash"},
    {"EventName": "CreateUser", "Username": "admin"},
    {"EventName": "DeleteTrail", "Username": "attacker"},
    {"EventName": "PutBucketPolicy", "Username": "developer"}
]

print("\nCLOUDTRAIL DETECTION REPORT\n")

for event in logs:

    event_name = event["EventName"]
    username = event["Username"]

    mitre_data = MITRE_MAP.get(event_name)

    technique = mitre_data["technique"]
    technique_name = mitre_data["name"]

    risk_score = calculate_risk(event_name)

    print("=" * 50)

    print(
        generate_summary(
            username,
            event_name,
            f"{technique} - {technique_name}",
            risk_score
        )
    )