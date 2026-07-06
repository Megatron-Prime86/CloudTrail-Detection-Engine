def detect(event):

    event_name = event["EventName"]

    if event_name == "CreateUser":
        return "MEDIUM - New IAM User Created"

    elif event_name == "DeleteTrail":
        return "CRITICAL - Possible Log Tampering"

    elif event_name == "PutBucketPolicy":
        return "HIGH - S3 Permission Change"

    elif event_name == "ConsoleLogin":
        return "INFO - User Login"

    return None