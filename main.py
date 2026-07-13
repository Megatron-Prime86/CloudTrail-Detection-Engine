from mitre_mapping import MITRE_MAP
from risk_score import calculate_risk
from incident_summary import generate_summary
from severity import get_severity
from detection_ids import DETECTION_IDS
from report_export import export_report
from event_categories import EVENT_CATEGORIES

from statistics import generate_statistics
from statistics_export import export_statistics
from statistics_report import print_statistics

import json

# Load CloudTrail logs
with open(
    "sample_cloudtrail_logs.json",
    "r"
) as file:

    logs = json.load(file)

report_data = []

print("\nCLOUDTRAIL DETECTION ENGINE v6.0\n")

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
        detection_id,
        timestamp,
        source_ip
    )

    print(report)

    report_data.append(
        {
            "detection_id": detection_id,
            "user": username,
            "source_ip": source_ip,
            "timestamp": timestamp,
            "event": event_name,
            "category": category,
            "severity": severity,
            "risk_score": risk_score,
            "mitre": technique,
            "tactic": tactic
        }
    )

# Export incident reports
export_report(
    report_data
)

# Generate security analytics
stats = generate_statistics(
    report_data
)

# Export analytics
export_statistics(
    stats
)

# Display analytics
print_statistics(
    stats
)

print(
    "\nReport exported to report.json"
)

print(
    "Statistics exported to security_statistics.json\n"
)
