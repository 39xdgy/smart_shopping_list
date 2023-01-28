from fastapi import APIRouter

from models.shopping_list import Shopping_list
from config.db import conn
from schemas.shopping_list import shoppingListEntity, shoppingListsEntity
from bson import ObjectId 


shopping_list = APIRouter()

@shopping_list.get('/')
async def find_all_shopping_list():
    return shoppingListsEntity(conn.shopping_list.list.find())

@shopping_list.get('/{id}')
async def find_one_shopping_list(id):
    return shoppingListEntity(conn.shopping_list.list.find_one({'_id': ObjectId(id)}))

@shopping_list.post('/')
async def create_shopping_list():
    new_id = conn.shopping_list.list.insert_one({"list": {}})
    return shoppingListEntity(conn.shopping_list.list.find_one({'_id': ObjectId(new_id.inserted_id)}))

@shopping_list.put('/{id}')
async def update_shopping_list(id, shopping_list: Shopping_list):
    conn.shopping_list.list.find_one_and_update({"_id": ObjectId(id)}, {
        "$set":dict(shopping_list)
    })
    return shoppingListEntity(conn.shopping_list.list.find_one({"_id": ObjectId(id)}))