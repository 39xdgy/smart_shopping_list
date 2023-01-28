from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson import ObjectId 

from routes.shopping_list import create_shopping_list


user = APIRouter()

@user.get('/')
async def find_all_user():
    #print(conn.shopping_list.user.find())  address of the object
    #print(usersEntity(conn.shopping_list.user.find()))   actual data
    return usersEntity(conn.shopping_list.user.find())

@user.get('/{id}')
async def find_one_user(id):
    return userEntity(conn.shopping_list.user.find_one({'_id': ObjectId(id)}))

@user.post('/')
async def create_user(user: User):
    output_json = await create_shopping_list()
    print(output_json)
    dict_user = dict(user)
    dict_user["list_id"] = str(output_json["id"])
    conn.shopping_list.user.insert_one(dict_user)
    return usersEntity(conn.shopping_list.user.find())

@user.put('/{id}')
async def update_user(id, user: User):
    conn.shopping_list.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set":dict(user)
    })
    return userEntity(conn.shopping_list.user.find_one({"_id": ObjectId(id)}))
'''
@user.patch('/{id}')
async def patch_user(id, info: User):
    conn.shopping_list.user.find_one_and_update(filter, update)
'''
@user.delete('/{id}')
async def delete_user(id):
    return userEntity(conn.shopping_list.user.find_one_and_delete({"_id": ObjectId(id)}))