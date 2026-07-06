import json

def export_report(report_data):

    with open(
        "report.json",
        "w"
    ) as file:

        json.dump(
            report_data,
            file,
            indent=4
        )
