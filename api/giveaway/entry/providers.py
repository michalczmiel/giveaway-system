import os
import json
from abc import ABC, abstractmethod

import boto3

from api.giveaway.entry.models import GiveawayEntry


class NotifyProvider(ABC):
    @abstractmethod
    def notify_giveaway_entered(self, entry: GiveawayEntry):
        pass


class SnsNotifyProvider(NotifyProvider):
    def __init__(self):
        self._sns = boto3.client("sns")
        self._topic_arn = os.environ["ENTRIES_SNS_TOPIC_ARN"]

    def notify_giveaway_entered(self, entry: GiveawayEntry):
        self._sns.publish(
            TopicArn=self._topic_arn,
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
