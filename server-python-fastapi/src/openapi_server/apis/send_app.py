from openapi_server.apis.programs_api_base import BaseProgramsApi
from openapi_server.models.application import Application
import logging


LOG = logging.getLogger(__name__)

class SendApi(BaseProgramsApi):
    async def send_app(self, application: Application) -> None:
        LOG.warning("In child")
