


class Register_Service:
    def __init__(self) -> None:
        passfrom pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.security import Auth
from models.user import User
from schemas.auth_schema import RegisterCreate, UserUpdateSchema


class AuthRepo:
    def __init__(self,session:AsyncSession) -> None:
        self.db=session

    async def get_user_by_email(self,email:EmailStr):
        user=(await self.db.execute(select(User).where(User.email==email))).scalar_one_or_none()
        return user

    async def create_user(self,data:RegisterCreate):
        user=User(
            full_name=data.full_name,
            email=data.email,
            password=Auth().hash.hash(data.password1)
        )
        self.db.add(user)
        await self.db.commit()
        return user

    async def update_user(self,data:UserUpdateSchema,user:User):
        for key,value in data.model_dump(exclude_unset=True).items():
            setattr(user,key,value)
        await self.db.commit()
        return True
