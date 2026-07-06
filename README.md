# CloudTrail Detection Engine

A Python-based Cloud Security Detection Engine that analyzes AWS CloudTrail events and transforms them into structured SOC-style incident reports.

The project is designed to simulate the workflow of a Security Operations Center (SOC) analyst by identifying cloud security events, mapping them to MITRE ATT&CK techniques, assigning risk scores, classifying event severity, and exporting investigation results in a structured format.

---

## Overview

CloudTrail Detection Engine processes AWS CloudTrail events and provides:

- Event Detection
- MITRE ATT&CK Mapping
- Risk Scoring
- Severity Classification
- Detection IDs
- Automated Incident Summaries
- JSON Report Export

The goal of this project is to bridge cloud security monitoring and security operations workflows through automation.

---

## Features

### Version 1.0 – Initial Detection Engine

- CloudTrail Event Processing
- Event Analysis
- Detection of Security-Relevant Activities

Supported Events:

- ConsoleLogin
- CreateUser
- DeleteTrail
- PutBucketPolicy

---

### Version 2.0 – Security Analysis Layer

- MITRE ATT&CK Technique Mapping
- Risk Score Calculation
- Automated Incident Summaries

Supported MITRE Techniques:

| Event | MITRE Technique |
|---------|---------|
| ConsoleLogin | T1078 - Valid Accounts |
| CreateUser | T1136 - Create Account |
| DeleteTrail | T1562 - Impair Defenses |
| PutBucketPolicy | T1098 - Account Manipulation |

---

### Version 3.0 – Reporting Engine

- Severity Classification
- Detection IDs
- Structured Reporting
- JSON Report Export

#### Severity Levels

| Risk Score | Severity |
|------------|------------|
| 90 - 100 | CRITICAL |
| 70 - 89 | HIGH |
| 40 - 69 | MEDIUM |
| 0 - 39 | LOW |

#### Detection IDs

| Event | Detection ID |
|---------|---------|
| ConsoleLogin | CT-001 |
| CreateUser | CT-002 |
| DeleteTrail | CT-003 |
| PutBucketPolicy | CT-004 |

---

## Project Structure

```text
cloudtrail-detection-engine/

├── main.py
├── mitre_mapping.py
├── risk_score.py
├── severity.py
├── detection_ids.py
├── incident_summary.py
├── report_export.py
├── report.json
└── README.md
```

---

## Example Output

```text
==================================================

INCIDENT SUMMARY

Detection ID:
CT-003

User:
attacker

Event:
DeleteTrail

Severity:
CRITICAL

Risk Score:
95/100

MITRE ATT&CK:
T1562 - Impair Defenses

Recommendation:
Investigate the event and verify whether the activity was authorized.

==================================================
```

---

## Sample JSON Export

```json
[
    {
        "detection_id": "CT-003",
        "user": "attacker",
        "event": "DeleteTrail",
        "severity": "CRITICAL",
        "risk_score": 95,
        "mitre": "T1562 - Impair Defenses"
    }
]
```

---

## Technologies Used

- Python
- AWS CloudTrail Concepts
- MITRE ATT&CK Framework
- Cloud Security Monitoring
- SOC Investigation Workflows
- JSON Reporting

---

## Skills Demonstrated

- Cloud Security
- Detection Engineering
- Incident Response
- Threat Detection
- MITRE ATT&CK Mapping
- Python Automation
- Security Operations Center (SOC) Concepts
- Security Reporting

---

## Future Enhancements

### Version 4.0 (Planned)

- MITRE ATT&CK Tactic Mapping
- Event Categorization
- Timestamp Support
- Executive Summary Generation
- Improved Risk Analysis

### Future Roadmap

- Real AWS CloudTrail Integration
- AI-Powered Incident Summaries
- Threat Intelligence Enrichment
- Email Alerting
- Dashboard Integration
- Cloud Security Monitoring Automation

---

## Author

**Subash G**

Aspiring Cybersecurity Analyst | Blue Team & Cloud Security Enthusiast

GitHub: https://github.com/Megatron-Prime86

---

## Project Status

✅ Version 1.0 Complete  
✅ Version 2.0 Complete  
✅ Version 3.0 Complete  

🚀 Currently progressing toward Version 4.0
