






from fastapi import HTTPException

from Expense.repo.auth_repo import AuthRepo
from Expense.schema.auth_schema import RegisterCreate


class AuthService:
    def __init__(self,authrepo:AuthRepo) -> None:
        self.authrepo=authrepo

    async def register_service(self,data:RegisterCreate):
        user=await self.authrepo.get_user_by_email(data.email)
        if user:
            raise HTTPException(status_code=400,detail="User already exists")
        user=await self.authrepo.create_user(data)
        return True
