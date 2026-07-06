def generate_summary(
    username,
    event,
    mitre,
    tactic,
    category,
    risk_score,
    severity,
    detection_id,
    timestamp,
    source_ip
):

    return f"""
==================================================

INCIDENT SUMMARY

Detection ID:
{detection_id}

User:
{username}

Timestamp:
{timestamp}

Source IP:
{source_ip}

Event:
{event}

Category:
{category}

MITRE ATT&CK Technique:
{mitre}

MITRE ATT&CK Tactic:
{tactic}

Severity:
{severity}

Risk Score:
{risk_score}/100

Executive Summary:

A {severity.lower()} severity cloud security
event was detected involving the activity
'{event}'.

The activity falls under the
'{category}' category and maps to the
MITRE ATT&CK tactic '{tactic}'.

Indicators of Compromise (IOC)

User:
{username}

Source IP:
{source_ip}

Event:
{event}

Recommended Actions:

- Investigate the activity
- Verify authorization
- Review related AWS actions
- Validate account behavior

==================================================
"""
