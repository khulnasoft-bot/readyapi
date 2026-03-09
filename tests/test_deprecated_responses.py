import warnings

import pytest
from pydantic import BaseModel
from readyapi import ReadyAPI
from readyapi.exceptions import ReadyAPIDeprecationWarning
from readyapi.responses import ORJSONResponse, UJSONResponse
from readyapi.testclient import TestClient


class Item(BaseModel):
    name: str
    price: float


# ORJSON


def _make_orjson_app() -> ReadyAPI:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ReadyAPIDeprecationWarning)
        app = ReadyAPI(default_response_class=ORJSONResponse)

    @app.get("/items")
    def get_items() -> Item:
        return Item(name="widget", price=9.99)

    return app


def test_orjson_response_returns_correct_data():
    app = _make_orjson_app()
    client = TestClient(app)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ReadyAPIDeprecationWarning)
        response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"name": "widget", "price": 9.99}


def test_orjson_response_emits_deprecation_warning():
    with pytest.warns(ReadyAPIDeprecationWarning, match="ORJSONResponse is deprecated"):
        ORJSONResponse(content={"hello": "world"})


# UJSON


def _make_ujson_app() -> ReadyAPI:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ReadyAPIDeprecationWarning)
        app = ReadyAPI(default_response_class=UJSONResponse)

    @app.get("/items")
    def get_items() -> Item:
        return Item(name="widget", price=9.99)

    return app


def test_ujson_response_returns_correct_data():
    app = _make_ujson_app()
    client = TestClient(app)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ReadyAPIDeprecationWarning)
        response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"name": "widget", "price": 9.99}


def test_ujson_response_emits_deprecation_warning():
    with pytest.warns(ReadyAPIDeprecationWarning, match="UJSONResponse is deprecated"):
        UJSONResponse(content={"hello": "world"})
