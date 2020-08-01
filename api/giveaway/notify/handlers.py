import json

from api.giveaway.utils.lambda_types import LambdaEvent


def notify_on_entry(event: LambdaEvent, context):
    for entry in event["Records"]:
        data = json.loads(entry["Message"])
        if data["type"] == "GIVEAWAY_ENTERED":
            entry_email = data["attributes"]["email"]
            print(f"Sending email to {entry_email}")
