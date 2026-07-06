from mitre_mapping import MITRE_MAP
from risk_score import calculate_risk
from incident_summary import generate_summary
from severity import get_severity
from detection_ids import DETECTION_IDS
from report_export import export_report
from event_categories import EVENT_CATEGORIES
import json

with open(
    "sample_cloudtrail_logs.json",
    "r"
) as file:

    logs = json.load(file)

report_data = []

print("\nCLOUDTRAIL DETECTION ENGINE v4.0\n")

for event in logs:

    event_name = event["EventName"]
    username = event["Username"]

    timestamp = event["Timestamp"]
    source_ip = event["SourceIP"]

    mitre_data = MITRE_MAP.get(event_name)

    technique = (
        f"{mitre_data['technique']} - "
        f"{mitre_data['name']}"
    )

    tactic = mitre_data["tactic"]

    category = EVENT_CATEGORIES.get(
        event_name,
        "Unknown"
    )

    risk_score = calculate_risk(
        event_name
    )

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
        tactic,
        category,
        risk_score,
        severity,
        detection_id
    )

    print(report)

    report_data.append(
        {
            "detection_id": detection_id,
            "user": username,
            "event": event_name,
            "category": category,
            "severity": severity,
            "risk_score": risk_score,
            "mitre": technique,
            "tactic": tactic
        }
    )

export_report(report_data)

print("\nReport exported to report.json\n")
