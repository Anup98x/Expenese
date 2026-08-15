from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from core.config import settings
from dependencies.get_user import get_user
from dependencies.service_factory import get_auth_service
from models.user import User
from schemas.auth_schema import (
    LoginSchema,
    RefreshSchema,
    RegisterCreate,
    UserReadSchema,
    UserUpdateSchema,
)
from schemas.common import SuccessResponse
from services.auth_services import AuthService

auth_api = APIRouter(prefix="/auth", tags=["Regsiter endpoints"])


@auth_api.post("/register", response_model=SuccessResponse[None])
async def create_user_endpoint(
    data: RegisterCreate, service: Annotated[AuthService, Depends(get_auth_service)]
):
    return await service.register_service(data)


@auth_api.post("/login")
async def login_user_endpoint(
    data: LoginSchema, service: Annotated[AuthService, Depends(get_auth_service)]
):
    return await service.login_service(data)


@auth_api.get("/me", response_model=SuccessResponse[UserReadSchema])
async def read_user_endpoint(user: Annotated[User, Depends(get_user)]):
    return SuccessResponse(data=user)


@auth_api.patch("/user", response_model=SuccessResponse[None])
async def update_user_endpoint(
    data: UserUpdateSchema,
    user: Annotated[User, Depends(get_user)],
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    return await auth_service.update_user_service(data, user)


@auth_api.post("/logout")
async def logout_user_endpoint():
    response = JSONResponse(
        status_code=200,
        content=SuccessResponse(message="Logout success", data=None).model_dump(),
    )
    response.delete_cookie(
        key=settings.LOGIN_COOKIE_NAME,
        path=settings.LOGIN_COOKIE_PATH,
        samesite=settings.SAME_SITE,
        secure=settings.SECURE,
    )
    return response


@auth_api.post("/refresh", response_model=SuccessResponse[RefreshSchema])
async def refresh_user_endpoint(
    request: Request, auth_service: Annotated[AuthService, Depends(get_auth_service)]
):
    return await auth_service.refresh_service(request)
