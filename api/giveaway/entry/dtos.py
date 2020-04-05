from uuid import UUID, uuid4
from datetime import datetime
from dataclasses import dataclass

from api.giveaway.common.dtos import Dto
from api.giveaway.entry.models import GiveawayEntry


@dataclass(frozen=True)
class GiveawayEntryInputDto(Dto):
    first_name: str
    last_name: str
    email: str
    gdpr_accepted: bool

    def map_to_model(self) -> GiveawayEntry:
        return GiveawayEntry(
            id=uuid4(),
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            gdpr_accepted=self.gdpr_accepted,
            created_at=datetime.utcnow(),
        )


@dataclass(frozen=True)
class GiveawayEntryOutputDto(Dto):
    id: UUID
    first_name: str
    last_name: str
    email: str
    gdpr_accepted: bool
    created_at: datetime

    @classmethod
    def map_from(cls, model: GiveawayEntry) -> "GiveawayEntryOutputDto":
        return GiveawayEntryOutputDto(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            email=model.email,
            gdpr_accepted=model.gdpr_accepted,
            created_at=model.created_at,
        )
