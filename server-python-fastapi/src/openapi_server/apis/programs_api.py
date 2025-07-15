# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.programs_api_base import BaseProgramsApi
from openapi_server.apis.send_app import SendApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field
from typing import Any
from typing_extensions import Annotated
from openapi_server.models.application import Application
import logging

LOG = logging.getLogger(__name__)


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/sendApp",
    responses={
        200: {"description": "For valid requests."},
        400: {"description": "Returned if any request parameters fail validation."},
        401: {"description": "Returned if the API key is invalid or does not have access to the program."},
    },
    tags=["programs"],
    summary="Send App",
    response_model_by_alias=True,
)
async def send_app(
    application: Annotated[Application, Field(description="The revision state of applications to include in results. When omitted, applications of all revision states are returned.")] = Body(None, description="The revision state of applications to include in results. When omitted, applications of all revision states are returned."),
) -> None:
    """Send app"""
    if not BaseProgramsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProgramsApi.subclasses[0]().send_app(application)
