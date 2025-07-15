# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field
from typing import Any
from typing_extensions import Annotated
from openapi_server.models.application import Application


class BaseProgramsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseProgramsApi.subclasses = BaseProgramsApi.subclasses + (cls,)
    async def send_app(
        self,
        application: Annotated[Application, Field(description="The revision state of applications to include in results. When omitted, applications of all revision states are returned.")],
    ) -> None:
        """Send app"""
        ...
