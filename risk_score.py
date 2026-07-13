def calculate_risk(event_name):

    scores = {

        "ConsoleLogin": 20,

        "CreateUser": 70,

        "DeleteTrail": 95,

        "PutBucketPolicy": 80,

        "CreateBucket": 40

    }

    return scores.get(
        event_name,
        10
    )