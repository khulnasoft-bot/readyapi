from typing import Annotated

from pydantic.v1 import BaseModel
from readyapi import ReadyAPI
from readyapi.temp_pydantic_v1_params import Body


class Item(BaseModel):
    name: str
    description: str | None = None
    size: float


app = ReadyAPI()


@app.post("/items/")
async def create_item(item: Annotated[Item, Body(embed=True)]) -> Item:
    return item
