import json


def export_statistics(stats):

    with open(
        "security_statistics.json",
        "w"
    ) as file:

        json.dump(
            stats,
            file,
            indent=4
        )