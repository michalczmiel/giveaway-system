import json
import dataclasses
import uuid
import datetime
from typing import Any, Dict
from http import HTTPStatus


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

def create_response(data: Any, status_code: HTTPStatus = HTTPStatus.OK) -> Response:
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True,
    }

    return {
        "body": json.dumps(data, cls=EnhancedJSONEncoder),
        "statusCode": status_code.value,
        "headers": headers,
    }
