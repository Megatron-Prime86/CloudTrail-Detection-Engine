DETECTION_RULES = {

    "DeleteTrail": {
        "alert": "CloudTrail Tampering Detected",
        "severity_override": "CRITICAL"
    },

    "CreateUser": {
        "alert": "New IAM User Created",
        "severity_override": "HIGH"
    },

    "PutBucketPolicy": {
        "alert": "S3 Permission Modification",
        "severity_override": "HIGH"
    },

    "CreateBucket": {
        "alert": "New S3 Bucket Created",
        "severity_override": None
    }

}
`