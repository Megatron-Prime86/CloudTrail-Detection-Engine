import json


def export_report(report_data):

    # JSON Export
    with open(
        "report.json",
        "w"
    ) as json_file:

        json.dump(
            report_data,
            json_file,
            indent=4
        )

    # TXT Export
    with open(
        "incident_report.txt",
        "w"
    ) as txt_file:

        txt_file.write(
            "CLOUDTRAIL DETECTION ENGINE REPORT\n"
        )

        txt_file.write(
            "=" * 60 + "\n\n"
        )

        for report in report_data:

            txt_file.write(
                f"Detection ID: "
                f"{report['detection_id']}\n"
            )

            txt_file.write(
                f"User: "
                f"{report['user']}\n"
            )

            txt_file.write(
                f"Event: "
                f"{report['event']}\n"
            )

            txt_file.write(
                f"Category: "
                f"{report['category']}\n"
            )

            txt_file.write(
                f"Severity: "
                f"{report['severity']}\n"
            )

            txt_file.write(
                f"Risk Score: "
                f"{report['risk_score']}/100\n"
            )

            txt_file.write(
                f"MITRE Technique: "
                f"{report['mitre']}\n"
            )

            txt_file.write(
                f"MITRE Tactic: "
                f"{report['tactic']}\n"
            )

            txt_file.write(
                "-" * 60 + "\n"
            )

    print("JSON report exported to report.json")
    print("TXT report exported to incident_report.txt")
