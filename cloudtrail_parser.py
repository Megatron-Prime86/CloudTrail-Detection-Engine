def parse_event(event):

    username = (
        event.get(
            "userIdentity",
            {}
        ).get(
            "arn",
            "Unknown"
        )
    )

    return {

        "EventName":
        event.get(
            "eventName",
            "Unknown"
        ),

        "Username":
        username,

        "SourceIP":
        event.get(
            "sourceIPAddress",
            "Unknown"
        ),

        "Timestamp":
        event.get(
            "eventTime",
            "Unknown"
        )
    }