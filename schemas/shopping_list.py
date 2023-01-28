def shoppingListEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "list": item["list"]
    }

def shoppingListsEntity(entity) -> list:
    return [shoppingListEntity(item) for item in entity]