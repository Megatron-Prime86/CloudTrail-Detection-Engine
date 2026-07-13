from collections import Counter


def generate_statistics(report_data):

    severity_counter = Counter()
    event_counter = Counter()
    tactic_counter = Counter()

    for report in report_data:

        severity_counter[
            report["severity"]
        ] += 1

        event_counter[
            report["event"]
        ] += 1

        tactic_counter[
            report["tactic"]
        ] += 1

    return {

        "total_events":
        len(report_data),

        "critical":
        severity_counter["CRITICAL"],

        "high":
        severity_counter["HIGH"],

        "medium":
        severity_counter["MEDIUM"],

        "low":
        severity_counter["LOW"],

        "most_common_event":
        event_counter.most_common(1)[0][0]
        if event_counter else "None",

        "most_common_tactic":
        tactic_counter.most_common(1)[0][0]
        if tactic_counter else "None"
    }