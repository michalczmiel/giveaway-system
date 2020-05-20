from typing import Any, Dict


def to_json_api(dto: Any, resource_type: str) -> Dict:
    data = {
        "id": dto.id,
        "type": resource_type,
        "attributes": dto,
    }

    return {
        "data": data,
    }
