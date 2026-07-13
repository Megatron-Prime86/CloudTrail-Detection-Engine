from mitre_mapping import MITRE_MAP
from risk_score import calculate_risk
from incident_summary import generate_summary
from severity import get_severity
from detection_ids import DETECTION_IDS
from report_export import export_report
from event_categories import EVENT_CATEGORIES
from cloudtrail_parser import parse_event
from detection_rules import DETECTION_RULES
from statistics import generate_statistics
from statistics_export import export_statistics
from statistics_report import print_statistics

import json

# Load real CloudTrail logs
with open(
    "real_cloudtrail_logs.json",
    "r"
) as file:

    logs = json.load(file)

report_data = []

print("\nCLOUDTRAIL DETECTION ENGINE v7.0\n")

for raw_event in logs:

    # Parse raw CloudTrail event
    event = parse_event(
        raw_event
    )

    event_name = event["EventName"]
    username = event["Username"]

    timestamp = event["Timestamp"]
    source_ip = event["SourceIP"]

    # Handle unknown events gracefully
    mitre_data = MITRE_MAP.get(
        event_name,
        {
            "technique": "Unknown",
            "name": "Unknown Activity",
            "tactic": "Unknown"
        }
    )

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
        event_name,
        "CT-000"
    )
    rule = DETECTION_RULES.get(
    event_name,
    {
        "alert": "Generic Cloud Event",
        "severity_override": None
    }
    )

    alert_name = rule["alert"]

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
    source_ip,
    alert_name
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

# Export reports
export_report(
    report_data
)

# Generate analytics
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
