from fastapi import FastAPI

from Expense.api.auth_api import auth_api


app=FastAPI()
app.include_router(auth_api)
