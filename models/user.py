from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str
    list_id: str
    