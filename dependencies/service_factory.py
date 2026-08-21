






from typing import Annotated

from fastapi import Depends

from Expense.dependencies.repo_factory import get_auth_repo, get_expense_repo
from Expense.repo.auth_repo import AuthRepo
from Expense.repo.expense_repo import ExpenseRepo
from Expense.service.auth_service import AuthService
from Expense.service.expense_service import ExpenseService


def get_expense_service(expense_repo:Annotated[ExpenseRepo,Depends(get_expense_repo)]):
    return ExpenseService(expense_repo)
def get_auth_service(auth_repo:Annotated[AuthRepo,Depends(get_auth_repo)]):
    return AuthService(authrepo=auth_repo)
