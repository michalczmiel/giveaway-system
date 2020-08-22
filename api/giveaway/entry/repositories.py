import os
from uuid import UUID
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict

import boto3

from api.giveaway.entry.models import GiveawayEntry
from api.giveaway.common.exceptions import NotFound


class GiveawayEntryRepository(ABC):
    @abstractmethod
    def persist(self, giveaway_entry: GiveawayEntry) -> GiveawayEntry:
        pass

    @abstractmethod
    def get(self, giveaway_entry: UUID) -> GiveawayEntry:
        pass


class DynamoDbGiveawayEntryRepository(GiveawayEntryRepository):
    def __init__(self):
        dynamodb = boto3.resource("dynamodb")
        self._table = dynamodb.Table(os.environ["ENTRIES_TABLE_NAME"])

    def to_model(self, item: Dict) -> GiveawayEntry:
        return GiveawayEntry(
            id=UUID(item["id"]),
            first_name=item["first_name"],
            last_name=item["last_name"],
            email=item["email"],
            gdpr_accepted=item["gdpr_accepted"],
            created_at=datetime.strptime(
                item["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            ),
        )

    def persist(self, giveaway_entry: GiveawayEntry) -> GiveawayEntry:
        item = {
            "id": str(giveaway_entry.id),
            "first_name": giveaway_entry.first_name,
            "last_name": giveaway_entry.last_name,
            "email": giveaway_entry.email,
            "gdpr_accepted": giveaway_entry.gdpr_accepted,
            "created_at": giveaway_entry.created_at.isoformat(),
        }
        self._table.put_item(Item=item)
        return giveaway_entry

    def get(self, giveaway_entry_id: UUID) -> GiveawayEntry:
        result = self._table.get_item(Key={"id": str(giveaway_entry_id)})

        if "Item" not in result:
            raise NotFound("GiveawayEntry not found")

        item = result["Item"]
        return self.to_model(item)
