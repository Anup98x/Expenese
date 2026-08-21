


from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from Expense.dependencies.service_factory import get_auth_service
from Expense.service.auth_service import AuthService
from Expense.schema.auth_schema import RegisterCreate


auth_api=APIRouter(prefix="/auth",tags=["Auth Endpoints"])

@auth_api.post("/register")
async def register_user_endpoint(data:RegisterCreate,service:Annotated[AuthService,Depends(get_auth_service)]):
    user=await service.register_service(data)
    if user:
        return JSONResponse(status_code=200,content="User created")
