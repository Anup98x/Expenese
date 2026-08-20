from email.mime import base

from click import echo
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import declarative_base
#from core.config import settings
from Expense.core.db import SessionHandler
from core.config import settings

#engine build
engine=create_async_engine(settings.DATABASE_URL,echo=True)
#session handler
SessionHandler=async_sessionmaker(
    bind=engine,#it gives path to datbase
    expire_on_commit=True, #if datbase row changes then python object(Table row value also changes)
    autoflush=False #if python object changes then database row doesnt automatically changes we need to change ourself
)
base=declarative_base() #base uses the property of declartive base sql alchemcy detects which class is model
async def get_db():
    async with SessionHandler() as db:
        yield db
