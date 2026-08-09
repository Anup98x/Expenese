from fastapi import FastAPI

from api.registerapi import registerapi
app=FastAPI()
app.include_router(registerapi)

