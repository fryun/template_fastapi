from typing import List
import os
from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.delivery import router
from app.core.config import config, gunicorn_config
from app.core.exceptions import CustomException
from app.core.fastapi.middlewares import ResponseLogMiddleware
from app.core.utils.logger import get_logger


logger = get_logger(__name__)


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def init_listeners(app_: FastAPI) -> None:

    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):

        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(ResponseLogMiddleware),
        
    ]
    return middleware


async def on_start_up() -> None:
    gunicorn_run = os.getenv("GUNICORN_RUN", False)
    if not gunicorn_run:
        config.DEBUG = True
    else:
        logger.info(f"total workers = {gunicorn_config.WORKERS}")

    logger.info(f"app env: {config.ENV}")
    logger.info(f"Debug: {config.DEBUG}")


async def on_shutdown() -> None:
    logger.info("Closing applications...")


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Template API",
        description="The template for API Project",
        version="1.0.0",
        docs_url=None if config.ENV == "prd" else "/docs",
        redoc_url=None if config.ENV == "prd" else "/redoc",
        middleware=make_middleware(),
        on_startup=[on_start_up],
        on_shutdown=[on_shutdown]
    )
    init_routers(app_=app_)
    init_listeners(app_=app_)
    return app_


# set logger
app = create_app()
