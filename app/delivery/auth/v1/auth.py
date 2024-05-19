
from fastapi import APIRouter

from app.usecase.sample_usecase import sample_case
from app.usecase.auth import login_for_access_token, read_users_me, read_own_items
from app.schema.auth import User

auth_router = APIRouter(prefix="/auth")


auth_router.add_api_route(
    "/token",
    login_for_access_token,
    methods=['POST'],
    response_model=None,
)

auth_router.add_api_route(
    "/users/me",
    login_for_access_token,
    methods=['GET'],
    response_model=None,
)

auth_router.add_api_route(
    "/users/me/items",
    read_own_items,
    methods=['GET'],
    response_model=User,
)

