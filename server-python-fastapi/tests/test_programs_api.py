# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.result import Result  # noqa: F401


def test_list_applications(client: TestClient):
    """Test case for list_applications

    Export applications
    """
    params = [("from_date", 'from_date_example'),     ("to_date", 'to_date_example'),     ("revision_state", 'revision_state_example'),     ("page_size", 56),     ("next_page_token", 'next_page_token_example')]
    headers = {
        "Authorization": "BasicZm9vOmJhcg==",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/applications",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

