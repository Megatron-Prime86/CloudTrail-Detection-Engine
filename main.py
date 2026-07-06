from mitre_mapping import MITRE_MAP
from risk_score import calculate_risk
from incident_summary import generate_summary
from severity import get_severity
from detection_ids import DETECTION_IDS
from report_export import export_report

logs = [
    {
        "EventName": "ConsoleLogin",
        "Username": "subash"
    },
    {
        "EventName": "CreateUser",
        "Username": "admin"
    },
    {
        "EventName": "DeleteTrail",
        "Username": "attacker"
    },
    {
        "EventName": "PutBucketPolicy",
        "Username": "developer"
    }
]

report_data = []

print("\nCLOUDTRAIL DETECTION ENGINE v3.0\n")

for event in logs:

    event_name = event["EventName"]
    username = event["Username"]

    mitre_data = MITRE_MAP.get(event_name)

    technique = (
        f"{mitre_data['technique']} - "
        f"{mitre_data['name']}"
    )

    risk_score = calculate_risk(event_name)

    severity = get_severity(
        risk_score
    )

    detection_id = DETECTION_IDS.get(
        event_name
    )

    report = generate_summary(
        username,
        event_name,
        technique,
        risk_score,
        severity,
        detection_id
    )

    print(report)

    report_data.append(
        {
            "detection_id":
            detection_id,

            "user":
            username,

            "event":
            event_name,

            "severity":
            severity,

            "risk_score":
            risk_score,

            "mitre":
            technique
        }
    )

export_report(report_data)

print(
    "\nReport exported to report.json\n"
)
