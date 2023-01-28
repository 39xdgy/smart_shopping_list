from pydantic import BaseModel

class Shopping_list(BaseModel):
    list: dict
    