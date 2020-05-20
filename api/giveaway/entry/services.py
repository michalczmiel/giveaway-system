import uuid

from api.giveaway.entry.dtos import (
    GiveawayEntryInputDto,
    GiveawayEntryOutputDto,
)
from api.giveaway.entry.repositories import DynamoDbGiveawayEntryRepository


class GiveawayService:
    @classmethod
    def create_giveaway_entry(
        cls, input_dto: GiveawayEntryInputDto
    ) -> GiveawayEntryOutputDto:
        giveaway_entry = input_dto.map_to_model()

        DynamoDbGiveawayEntryRepository.persist(giveaway_entry)

        return GiveawayEntryOutputDto.map_from(giveaway_entry)

    @classmethod
    def get_giveaway_entry(
        cls, giveaway_entry_id: uuid.UUID
    ) -> GiveawayEntryOutputDto:
        giveaway_entry = DynamoDbGiveawayEntryRepository.get(giveaway_entry_id)

        return GiveawayEntryOutputDto.map_from(giveaway_entry)
