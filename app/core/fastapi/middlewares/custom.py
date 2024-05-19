
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from typing import Callable
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware

async def process_request(request: Request, call_next):
    # Tugas pra-pemrosesan sebelum permintaan masuk
    response = await call_next(request)  # Melanjutkan ke route handler
    # Tugas pascapemrosesan setelah route handler selesai

    return response

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:

        # Tugas pra-pemrosesan sebelum permintaan masuk
        response = await call_next(request)  # Melanjutkan ke route handler
        # Tugas pascapemrosesan setelah route handler selesai

        return response

class BackgroundTaskExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable
    ) -> JSONResponse:
        try:
            response = await call_next(request)
        except StarletteHTTPException as http_exception:
            return JSONResponse(
                status_code=http_exception.status_code,
                content={"detail": http_exception.detail},
            )
        except RequestValidationError as validation_exception:
            return JSONResponse(
                status_code=422,
                content={"detail": "Validation Error"},
            )
        except Exception as exception:
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error"},
            )
        return response