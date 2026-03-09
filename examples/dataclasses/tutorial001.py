from dataclasses import dataclass

from readyapi import ReadyAPI


@dataclass
class Item:
    name: str
    price: float
    description: str | None = None
    tax: float | None = None


app = ReadyAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
