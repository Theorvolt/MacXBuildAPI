import motor.motor_asyncio
from bson.objectid import ObjectId 
from decouple import config

MONGO_DB = config("MONGO")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)


database = client.notes 
user_collection = database.get_collection("user_collection")


def formatter(user):

    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "password": user["password"]
    }

async def retrieve_users():
    return [formatter(user) async for user in user_collection.find()]


async def add_user(data: dict) -> dict:
    user = await user_collection.insert_one(data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})

    return formatter(new_user)

async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)}) # This is going to return empty if the user doesn't exist

    if user: 
        await user_collection.delete_one({"_id":  ObjectId(id)})

async def retrieve_user(id: str):

    user = await user_collection.find_one({"_id": user.inserted_id})

    if user:
        return user

async def update_user(id: str, data: dict):

    # if our data is empty, return nothing
    if not data:
        return False 
    
    user = await user_collection.find_one({"_id": user.inserted_id})

    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set", data}
        )

        if updated_user:
            return True 
        return False 
