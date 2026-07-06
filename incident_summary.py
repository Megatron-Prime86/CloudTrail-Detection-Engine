def generate_summary(username, event, mitre, score):

    return f"""
INCIDENT SUMMARY

User: {username}
Event: {event}

MITRE ATT&CK:
{mitre}

Risk Score:
{score}/100

Recommendation:
Investigate the event and verify whether the activity was authorized.
"""