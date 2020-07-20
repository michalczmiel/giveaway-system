import json
import dataclasses
import uuid
import datetime
from typing import Any, Dict

from pydantic import ValidationError


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o: Any):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if isinstance(o, uuid.UUID):
            return str(o)
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        return super().default(o)


Response = Dict


def to_json(data: Any) -> str:
    if isinstance(data, ValidationError):
        return data.json()
    return json.dumps(data, cls=EnhancedJSONEncoder)


def create_response(data: Any, status_code: int) -> Response:
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True,
    }

    return {
        "body": to_json(data),
        "statusCode": status_code,
        "headers": headers,
    }
