import uuid

from api.giveaway.entry.dtos import (
    GiveawayEntryInputDto,
    GiveawayEntryOutputDto,
)
from api.giveaway.entry.repositories import GiveawayEntryRepository
from api.giveaway.entry.providers import NotifyProvider


class GiveawayService:
    def __init__(
        self,
        giveaway_repository: GiveawayEntryRepository,
        notify_provider: NotifyProvider,
    ):
        self._giveaway_repository = giveaway_repository
        self._notify_provider = notify_provider

    def create_giveaway_entry(
        self, input_dto: GiveawayEntryInputDto
    ) -> GiveawayEntryOutputDto:
        giveaway_entry = input_dto.map_to_model()

        self._giveaway_repository.persist(giveaway_entry)

        self._notify_provider.notify_giveaway_entered(giveaway_entry)

        return GiveawayEntryOutputDto.map_from(giveaway_entry)

    def get_giveaway_entry(
        self, giveaway_entry_id: uuid.UUID
    ) -> GiveawayEntryOutputDto:
        giveaway_entry = self._giveaway_repository.get(giveaway_entry_id)

        return GiveawayEntryOutputDto.map_from(giveaway_entry)
