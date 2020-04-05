import json
from http import HTTPStatus

from api.giveaway.utils.json_api import to_json_api
from api.giveaway.utils.response import create_response, Response
from api.giveaway.utils.lambda_types import LambdaEvent
from api.giveaway.entry.services import GiveawayService
from api.giveaway.entry.dtos import GiveawayEntryInputDto


def create_giveaway_entry(event: LambdaEvent, context) -> Response:
    data = json.loads(event["body"])
    attributes = data["data"]["attributes"]

    dto = GiveawayEntryInputDto(**attributes)

    giveaway_entry_dto = GiveawayService.create_giveaway_entry(input_dto=dto)

    result_json = to_json_api(giveaway_entry_dto, resource_type="giveaway-entry")

    return create_response(result_json, status_code=HTTPStatus.CREATED)


def get_giveaway_entry(event: LambdaEvent, context) -> Response:
    giveaway_entry_id = event["pathParameters"]["id"]

    giveaway_entry_dto = GiveawayService.get_giveaway_entry(giveaway_entry_id)

    result_json = to_json_api(giveaway_entry_dto, resource_type="giveaway-entry")

    return create_response(result_json, status_code=HTTPStatus.OK)
