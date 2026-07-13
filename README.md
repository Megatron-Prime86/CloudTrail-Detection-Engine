# CloudTrail Detection Engine

A Python-based Cloud Security Detection and Analytics Platform that analyzes AWS CloudTrail events and transforms them into structured SOC-style incident reports.

The project simulates the workflow of a Security Operations Center (SOC) analyst by ingesting AWS CloudTrail events, mapping activities to MITRE ATT&CK techniques, calculating risk scores, classifying event severity, extracting indicators of compromise (IOCs), generating incident reports, and producing security analytics.

---

# Overview

CloudTrail Detection Engine processes AWS CloudTrail events and provides:

- Event Detection
- MITRE ATT&CK Technique Mapping
- MITRE ATT&CK Tactic Mapping
- Risk Scoring
- Severity Classification
- Detection IDs
- IOC Extraction
- Automated Incident Summaries
- JSON Report Export
- TXT Report Export
- Security Analytics
- Real CloudTrail Event Support

The goal of the project is to transform raw AWS audit logs into actionable security intelligence.

---

# Features

## ✅ Version 1.0 – Initial Detection Engine

- CloudTrail Event Processing
- Event Analysis
- Detection of Security-Relevant Activities

Supported Events:

- ConsoleLogin
- CreateUser
- DeleteTrail
- PutBucketPolicy

---

## ✅ Version 2.0 – Security Analysis Layer

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

## ✅ Version 3.0 – Reporting Engine

- Severity Classification
- Detection IDs
- Structured Incident Reports
- JSON Report Export

### Severity Levels

| Risk Score | Severity |
|------------|------------|
| 90 - 100 | CRITICAL |
| 70 - 89 | HIGH |
| 40 - 69 | MEDIUM |
| 0 - 39 | LOW |

### Detection IDs

| Event | Detection ID |
|---------|---------|
| ConsoleLogin | CT-001 |
| CreateUser | CT-002 |
| DeleteTrail | CT-003 |
| PutBucketPolicy | CT-004 |
| CreateBucket | CT-005 |

---

## ✅ Version 4.0 – Threat Context Enrichment

- MITRE ATT&CK Tactic Mapping
- Event Categorization
- Enhanced Executive Summaries
- Human-Readable TXT Report Export

### MITRE ATT&CK Tactics

| Event | Tactic |
|---------|---------|
| ConsoleLogin | Initial Access |
| CreateUser | Persistence |
| DeleteTrail | Defense Evasion |
| PutBucketPolicy | Privilege Escalation |
| CreateBucket | Collection |

---

## ✅ Version 5.0 – Investigation & IOC Intelligence

- Timestamp Tracking
- Source IP Tracking
- IOC Extraction
- Investigation-Centric Reporting

### IOC Data

Each report contains:

- Username
- Event Type
- Timestamp
- Source IP Address
- Severity
- MITRE ATT&CK Mapping

---

## ✅ Version 6.0 – Security Analytics Layer

- Event Statistics
- Severity Distribution
- Most Common Event Tracking
- Most Common MITRE Tactic Tracking
- Security Dashboard Export

Generated Analytics:

- Total Events Analyzed
- Critical Events
- High Events
- Medium Events
- Low Events
- Most Common Event
- Most Common Tactic

---

## ✅ Version 7.0 – Real CloudTrail Event Ingestion

Version 7 introduces support for parsing and analyzing real AWS CloudTrail logs.

### New Capabilities

- Real AWS CloudTrail Event Support
- CloudTrail JSON Parsing
- Native AWS Event Processing
- Event Normalization Layer
- Real Event Ingestion Pipeline

### CloudTrail Parser

The parser converts native CloudTrail events into a normalized structure used by the detection engine.

### Supported CloudTrail Fields

| CloudTrail Field | Parsed Output |
|------------------|---------------|
| eventName | EventName |
| eventTime | Timestamp |
| sourceIPAddress | SourceIP |
| userIdentity.arn | Username |

### Example Real CloudTrail Event

```json
{
  "eventName": "CreateBucket",
  "eventTime": "2026-07-13T06:03:20Z",
  "sourceIPAddress": "106.51.210.98",
  "eventSource": "s3.amazonaws.com"
}
```

### Parsed Event

```json
{
  "EventName": "CreateBucket",
  "Username": "arn:aws:iam::ACCOUNT_ID:root",
  "SourceIP": "106.51.210.98",
  "Timestamp": "2026-07-13T06:03:20Z"
}
```

---

# Detection Workflow

```text
AWS CloudTrail Event
          ↓
CloudTrail Parser
          ↓
Detection Engine
          ↓
MITRE ATT&CK Mapping
          ↓
Risk Scoring
          ↓
Severity Classification
          ↓
IOC Extraction
          ↓
Security Analytics
          ↓
Report Generation
```

---

# Project Structure

```text
cloudtrail-detection-engine/

├── main.py
├── cloudtrail_parser.py

├── real_cloudtrail_logs.json
├── sample_cloudtrail_logs.json

├── mitre_mapping.py
├── event_categories.py
├── risk_score.py
├── severity.py
├── detection_ids.py

├── incident_summary.py
├── report_export.py

├── statistics.py
├── statistics_export.py
├── statistics_report.py

├── report.json
├── incident_report.txt
├── security_statistics.json

└── README.md
```

---

# Sample Security Analytics Output

```text
==================================================
SECURITY ANALYTICS SUMMARY
==================================================

Total Events Analyzed : 8

Critical Events       : 2
High Events           : 3
Medium Events         : 1
Low Events            : 2

Most Common Event     : CreateUser

Most Common Tactic    : Persistence

==================================================
```

---

# Technologies Used

- Python
- AWS CloudTrail
- MITRE ATT&CK Framework
- Cloud Security Monitoring
- Detection Engineering
- Security Analytics
- Incident Response Concepts
- JSON Processing

---

# Skills Demonstrated

- Cloud Security
- AWS Security Monitoring
- Detection Engineering
- MITRE ATT&CK Mapping
- Threat Detection
- Security Analytics
- Incident Response
- IOC Identification
- Security Reporting
- Python Automation

---

# Project Evolution

### ✅ Version 1.0
- Event Detection Engine

### ✅ Version 2.0
- MITRE ATT&CK Mapping
- Risk Scoring

### ✅ Version 3.0
- Severity Classification
- Detection IDs
- JSON Reporting

### ✅ Version 4.0
- MITRE ATT&CK Tactic Mapping
- Event Categorization
- TXT Reporting

### ✅ Version 5.0
- Source IP Tracking
- Timestamp Tracking
- IOC Extraction

### ✅ Version 6.0
- Security Analytics
- Severity Distribution
- Event Statistics

### ✅ Version 7.0
- Real CloudTrail Event Support
- CloudTrail Parser
- Real AWS Log Processing

---

# Future Roadmap

## 🔄 Version 8.0

- AWS CloudTrail API Integration (boto3)
- Automated Event Retrieval
- Continuous CloudTrail Monitoring

## 🔄 Version 9.0

- Threat Intelligence Enrichment
- IP Reputation Analysis
- IOC Correlation

## 🔄 Version 10.0

- Real-Time Alerting
- Email Notifications
- SOC Dashboard

---

# Author

**Subash G**

Aspiring Cybersecurity Analyst | Blue Team & Cloud Security Enthusiast

GitHub:
https://github.com/Megatron-Prime86

---

# Current Status

✅ Version 1.0 Complete  
✅ Version 2.0 Complete  
✅ Version 3.0 Complete  
✅ Version 4.0 Complete  
✅ Version 5.0 Complete  
✅ Version 6.0 Complete  
✅ Version 7.0 Complete  

🚀 Currently planning Version 8.0 – AWS CloudTrail API Integration