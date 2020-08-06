import os
from uuid import UUID
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict

import boto3

from api.giveaway.entry.models import GiveawayEntry
from api.giveaway.common.exceptions import NotFound


class GiveawayEntryRepository(ABC):
    @classmethod
    @abstractmethod
    def persist(cls, giveaway_entry: GiveawayEntry) -> GiveawayEntry:
        pass

    @classmethod
    @abstractmethod
    def get(cls, giveaway_entry: UUID) -> GiveawayEntry:
        pass


dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table(os.environ["ENTRIES_TABLE_NAME"])


class DynamoDbGiveawayEntryRepository(GiveawayEntryRepository):
    @classmethod
    def to_model(cls, item: Dict) -> GiveawayEntry:
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

    @classmethod
    def persist(cls, giveaway_entry: GiveawayEntry) -> GiveawayEntry:
        item = {
            "id": str(giveaway_entry.id),
            "first_name": giveaway_entry.first_name,
            "last_name": giveaway_entry.last_name,
            "email": giveaway_entry.email,
            "gdpr_accepted": giveaway_entry.gdpr_accepted,
            "created_at": giveaway_entry.created_at.isoformat(),
        }
        table.put_item(Item=item)
        return giveaway_entry

    @classmethod
    def get(cls, giveaway_entry_id: UUID) -> GiveawayEntry:
        result = table.get_item(Key={"id": str(giveaway_entry_id)})

        if "Item" not in result:
            raise NotFound("GiveawayEntry not found")

        item = result["Item"]
        return cls.to_model(item)
