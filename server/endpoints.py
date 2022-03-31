from fastapi import APIRouter, Body 
from fastapi.encoders import jsonable_encoder

from server.models import *
from db import *

router = APIRouter()


@router.get("/root", response_description="This is a test")
async def get_root():
    return "Hello!"


@router.get("/")
async def get_all_users():
    users = await retrieve_users()

    return users

@router.post("/")
async def post_user(data: User):
    new_user = await add_user(jsonable_encoder(data))

    return new_user

@router.delete("/")
async def del_user(id: str):
    deleted_user = await delete_user(id)

    return deleted_user

@router.put("/")
async def put_user(id: str, data: UpdateUser):
    filtered = {field: value for field,value in data.dict().items() if value is not None}
    updated_user = await update_user(id, filtered)

    return updated_user