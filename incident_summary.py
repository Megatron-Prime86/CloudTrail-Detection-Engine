def generate_summary(
    username,
    event,
    mitre,
    risk_score,
    severity,
    detection_id
):

    return f"""
==================================================

INCIDENT SUMMARY

Detection ID:
{detection_id}

User:
{username}

Event:
{event}

Severity:
{severity}

Risk Score:
{risk_score}/100

MITRE ATT&CK:
{mitre}

Recommendation:
Investigate the event and verify whether the activity was authorized.

==================================================
"""
`
