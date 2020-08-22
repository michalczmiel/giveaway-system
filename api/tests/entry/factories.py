import factory
from mimesis_factory import MimesisField

from api.giveaway.entry.dtos import GiveawayEntryInputDto


class GiveawayEntryInputDtoFactory(factory.Factory):
    class Meta:
        model = GiveawayEntryInputDto

    first_name = MimesisField("first_name")
    last_name = MimesisField("last_name")
    email = factory.LazyAttribute(
        lambda instance: '{0}{1}@example.org'.format(instance.first_name, instance.last_name)
    )
    gdpr_accepted = True
