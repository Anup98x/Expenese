from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_db
from repo.auth_repo import AuthRepo
from repo.category_repo import CategoryRepo
from repo.expense_repo import ExpenseRepo


def get_auth_repo(db:Annotated[AsyncSession,Depends(get_db)] ):
    return AuthRepo(db)

def get_expense_repo(db:Annotated[AsyncSession,Depends(get_db)]):
    return ExpenseRepo(db)

def get_category_repo(db:Annotated[AsyncSession,Depends(get_db)]):
    return CategoryRepo(db)
