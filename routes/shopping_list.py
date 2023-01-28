from fastapi import APIRouter

from models.shopping_list import Shopping_list
from config.db import conn
from schemas.shopping_list import shoppingListEntity, shoppingListsEntity
from bson import ObjectId 

from reader.amazon import amazon
from reader.walmart import walmart


shopping_list = APIRouter()

amazon_reader = amazon()
walmart_reader = walmart()

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
async def add_item(id, link, name, priority):
    new_shopping_list = shoppingListEntity(conn.shopping_list.list.find_one({"_id": ObjectId(id)}))
    item_info = {}
    if("amazon.com" in link):
        response = amazon_reader.fetch(link)
        if(response):
            item_info = {
                "full name": amazon_reader.get_name(),
                "price": amazon_reader.get_price(),
                "link": link,
                "priority": int(priority)
            }
        else:
            print("amazon fetch error")
    elif("walmart.com" in link):
        response = walmart_reader.fetch(link)
        if(response):
            item_info = {
                "full name": walmart_reader.get_name(),
                "price": walmart_reader.get_price(),
                "link": link,
                "priority": int(priority)
            }
        else:
            print("walmart fetch error")
    else:
        print("ERROR: link does not meet the stander")

    new_shopping_list["list"][name] = item_info
    conn.shopping_list.list.find_one_and_update({"_id": ObjectId(id)}, {
        "$set":new_shopping_list
    })
    return shoppingListEntity(conn.shopping_list.list.find_one({"_id": ObjectId(id)}))