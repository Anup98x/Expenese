from sqlalchemy.ext.asyncio import AsyncSession

from model.user import User


class UserRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: User):
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

        return user
