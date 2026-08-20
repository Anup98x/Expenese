from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from Expense.service.register import AuthRepo
from core.db import get_db
from repo.register import UserRepository


def get_auth_repo(db:Annotated[AsyncSession,Depends(get_db)]):
    return AuthRepo(db)
