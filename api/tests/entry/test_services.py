from unittest.mock import Mock

from api.giveaway.entry.services import GiveawayService
from api.giveaway.entry.repositories import GiveawayEntryRepository
from api.giveaway.entry.providers import NotifyProvider
from api.giveaway.entry.dtos import GiveawayEntryOutputDto
from api.tests.entry.factories import GiveawayEntryInputDtoFactory


class TestGiveawayService:
    def test_create_giveaway_entry(self):
        repository = Mock(spec_set=GiveawayEntryRepository)
        notify_provider = Mock(spec_set=NotifyProvider)

        giveaway_service = GiveawayService(
            giveaway_repository=repository,
            notify_provider=notify_provider
        )

        input_dto = GiveawayEntryInputDtoFactory.create()

        output_dto = giveaway_service.create_giveaway_entry(input_dto)

        repository.persist.assert_called_once()
        notify_provider.notify_giveaway_entered.assert_called_once()

        assert isinstance(output_dto, GiveawayEntryOutputDto)
        assert output_dto.first_name == input_dto.first_name
        assert output_dto.last_name == input_dto.last_name
        assert output_dto.email == input_dto.email
        assert output_dto.gdpr_accepted == input_dto.gdpr_accepted
        assert output_dto.id
        assert output_dto.created_at

