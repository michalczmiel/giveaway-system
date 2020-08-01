import os
import json
from abc import ABC, abstractmethod

import boto3

from api.giveaway.entry.models import GiveawayEntry

sns = boto3.client("sns")

ENTRIES_SNS_TOPIC_ARN = os.environ["ENTRIES_SNS_TOPIC_ARN"]


class NotifyProvider(ABC):
    @classmethod
    @abstractmethod
    def notify_giveaway_entered(cls, entry: GiveawayEntry):
        pass


class SnsNotifyProvider(NotifyProvider):
    @classmethod
    def notify_giveaway_entered(cls, entry: GiveawayEntry):
        sns.publish(
            TopicArn=ENTRIES_SNS_TOPIC_ARN,
            Message=json.dumps(
                {
                    "type": "GIVEAWAY_ENTERED",
                    "attributes": {
                        "email": entry.email,
                        "first_name": entry.first_name,
                    },
                }
            ),
        )
