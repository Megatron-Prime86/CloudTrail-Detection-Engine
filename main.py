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

# Handle single event JSON files
if isinstance(logs, dict):
    logs = [logs]

report_data = []

print("\nCLOUDTRAIL DETECTION ENGINE v7.1\n")

for raw_event in logs:

    # Parse CloudTrail event
    event = parse_event(
        raw_event
    )

    event_name = event["EventName"]
    username = event["Username"]

    timestamp = event["Timestamp"]
    source_ip = event["SourceIP"]

    # MITRE Mapping
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

    # Category
    category = EVENT_CATEGORIES.get(
        event_name,
        "Unknown"
    )

    # Risk Score
    risk_score = calculate_risk(
        event_name
    )

    # Severity
    severity = get_severity(
        risk_score
    )

    # Detection ID
    detection_id = DETECTION_IDS.get(
        event_name,
        "CT-000"
    )

    # Detection Rules
    rule = DETECTION_RULES.get(
        event_name,
        {
            "alert": "Generic Cloud Event",
            "severity_override": None
        }
    )

    alert_name = rule["alert"]

    # Report
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
            "alert": alert_name,
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

# Export Reports
export_report(
    report_data
)

# Analytics
stats = generate_statistics(
    report_data
)

# Export Statistics
export_statistics(
    stats
)

# Display Statistics
print_statistics(
    stats
)

print(
    "\nReport exported to report.json"
)

print(
    "Statistics exported to security_statistics.json\n"
)