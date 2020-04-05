import uuid
from datetime import datetime
from dataclasses import dataclass

from api.giveaway.common.models import Model


@dataclass(frozen=True)
class GiveawayEntry(Model):
    id: uuid.UUID
    first_name: str
    last_name: str
    gdpr_accepted: bool
    email: str
    created_at: datetime
