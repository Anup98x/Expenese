from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from Expense.repo.expense_repo import ExpenseRepo
from Expense.service.auth_service import AuthRepo
from Expense.core.db import get_db
from Expense.repo.auth_repo import AuthRepo

def get_auth_repo(db:Annotated[AsyncSession,Depends(get_db)]):
    return AuthRepo(db)

def get_expense_repo(db:Annotated[AsyncSession,Depends(get_db)]):
    return ExpenseRepo(db)
