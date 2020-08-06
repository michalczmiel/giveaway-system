from uuid import UUID, uuid4
from dataclasses import dataclass

from api.giveaway.utils.json_api import to_json_api
from api.giveaway.common.dtos import Dto


def test_to_json_api():
    @dataclass(frozen=True)
    class ExampleDto(Dto):
        id: UUID
        name: str

    dto = ExampleDto(id=uuid4(), name="name")

    result = to_json_api(dto, "resource")

    assert result["data"]
    assert result["data"]["id"]
    assert result["data"]["type"] == "resource"
    assert result["data"]["attributes"]
