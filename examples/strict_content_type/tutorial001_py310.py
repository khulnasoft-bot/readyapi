from pydantic import BaseModel
from readyapi import ReadyAPI

app = ReadyAPI(strict_content_type=False)


class Item(BaseModel):
    name: str
    price: float


@app.post("/items/")
async def create_item(item: Item):
    return item
