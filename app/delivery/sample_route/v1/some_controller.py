
from fastapi import APIRouter

from app.usecase.sample_usecase import sample_case

sample_router = APIRouter(prefix="/sample")


sample_router.add_api_route(
    "/case",
    sample_case,
    methods=['POST'],
    response_model=None,
)