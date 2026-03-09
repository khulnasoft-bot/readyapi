from pydantic.v1 import BaseModel
from readyapi import ReadyAPI


class Item(BaseModel):
    name: str
    description: str | None = None
    size: float


app = ReadyAPI()


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item
