import http
import datetime
from uuid import UUID

from api.giveaway.utils.response import create_response


def test_create_response():
    data = {
        "data": {
            "id": UUID("57265006-6a75-4901-ad17-0a82605634c0"),
            "type": "giveaway_entry",
            "attributes": {
                "id": UUID("57265006-6a75-4901-ad17-0a82605634c0"),
                "first_name": "Mike",
                "last_name": "Scott",
                "email": "mike@dunder.com",
                "gdpr_accepted": True,
                "created_at": datetime.datetime(2020, 2, 29, 13, 33, 3, 42504),
            },
        }
    }
    response = create_response(data, http.HTTPStatus.OK)

    assert response["body"]
    assert isinstance(response["body"], str)
    assert response["statusCode"]
    assert response["statusCode"] == http.HTTPStatus.OK
