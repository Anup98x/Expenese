


from fastapi import APIRouter

from schema.register import RegisterCreate

registerapi=APIRouter(prefix="/register",tags=["registerendpoints"])
@registerapi.post("/") #default route
async def register_end_points(data:RegisterCreate):
 pass
