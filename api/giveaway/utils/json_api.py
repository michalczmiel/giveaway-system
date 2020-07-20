from typing import Dict

from api.giveaway.common.dtos import Dto


def to_json_api(dto: Dto, resource_type: str) -> Dict:
    data = {
        "id": dto.id,
        "type": resource_type,
        "attributes": dto.dict(),
    }

    return {
        "data": data,
    }
