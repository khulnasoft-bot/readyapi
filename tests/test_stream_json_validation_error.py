from collections.abc import AsyncIterable, Iterable

import pytest
from pydantic import BaseModel
from readyapi import ReadyAPI
from readyapi.exceptions import ResponseValidationError
from readyapi.testclient import TestClient


class Item(BaseModel):
    name: str
    price: float


app = ReadyAPI()


@app.get("/items/stream-invalid")
async def stream_items_invalid() -> AsyncIterable[Item]:
    yield {"name": "valid", "price": 1.0}
    yield {"name": "invalid", "price": "not-a-number"}


@app.get("/items/stream-invalid-sync")
def stream_items_invalid_sync() -> Iterable[Item]:
    yield {"name": "valid", "price": 1.0}
    yield {"name": "invalid", "price": "not-a-number"}


client = TestClient(app)


def test_stream_json_validation_error_async():
    with pytest.raises(ResponseValidationError):
        client.get("/items/stream-invalid")


def test_stream_json_validation_error_sync():
    with pytest.raises(ResponseValidationError):
        client.get("/items/stream-invalid-sync")
