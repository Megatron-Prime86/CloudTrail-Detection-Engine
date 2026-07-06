def calculate_risk(event_name):

    scores = {
        "ConsoleLogin": 20,
        "CreateUser": 70,
        "PutBucketPolicy": 80,
        "DeleteTrail": 95
    }

    return scores.get(event_name, 10)