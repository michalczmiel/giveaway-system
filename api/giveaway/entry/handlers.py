import json
import http

from pydantic import ValidationError

from api.giveaway.utils.json_api import to_json_api
from api.giveaway.utils.response import create_response, Response
from api.giveaway.utils.lambda_types import LambdaEvent
from api.giveaway.entry.services import GiveawayService
from api.giveaway.entry.dtos import GiveawayEntryInputDto
from api.giveaway.common.exceptions import NotFound


def create_giveaway_entry(event: LambdaEvent, context) -> Response:
    data = json.loads(event["body"])
    attributes = data["data"]["attributes"]

    try:
        dto = GiveawayEntryInputDto(**attributes)
    except ValidationError as error:
        return create_response(error, status_code=http.HTTPStatus.BAD_REQUEST)

    giveaway_entry_dto = GiveawayService.create_giveaway_entry(input_dto=dto)

    result_json = to_json_api(
        giveaway_entry_dto, resource_type="giveaway-entry"
    )

    return create_response(result_json, status_code=http.HTTPStatus.CREATED)


def get_giveaway_entry(event: LambdaEvent, context) -> Response:
    giveaway_entry_id = event["pathParameters"]["id"]

    try:
        giveaway_entry_dto = GiveawayService.get_giveaway_entry(
            giveaway_entry_id
        )

        result_json = to_json_api(
            giveaway_entry_dto, resource_type="giveaway-entry"
        )

        return create_response(result_json, status_code=http.HTTPStatus.OK)
    except NotFound as exception:
        create_response(exception, status_code=http.HTTPStatus.NOT_FOUND)
