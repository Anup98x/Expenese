from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pwdlib import PasswordHash
from Expense.schema.auth_schema import RegisterCreate
from Expense.model.user import User


class AuthRepo:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_email(self,email:str):
        user=(await self.db.execute(select(User.email==email))).scalar_one_or_none()
        return user

    async def create_user(self,data:RegisterCreate):

        hash=PasswordHash.recommended()
        user=User(
            email=data.email,
            full_name=data.full_name,
            password=hash.hash(data.password1)
        )
        self.db.add(user)
        await self.db.commit()
        return user
