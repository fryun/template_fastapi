from types import ModuleType
import json

from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.core.utils.logger import get_logger
from app.core.config import config
from app.schema.some_schema import SamplePayload

logger = get_logger(__name__)


async def sample_case(request: Request, item:SamplePayload):

    param_req = dict(request.query_params)
    logger.info(f"[REQUEST RECEIVE] Get Step")
    logger.info(f"param request: {json.dumps(param_req, indent=4)}")

    return JSONResponse(content={
                                "status": "Success",
                                },
                        status_code=status.HTTP_200_OK)
