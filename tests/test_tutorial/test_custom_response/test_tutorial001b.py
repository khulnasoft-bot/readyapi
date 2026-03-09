import warnings

import pytest
from inline_snapshot import snapshot
from readyapi.exceptions import ReadyAPIDeprecationWarning
from readyapi.testclient import TestClient

with warnings.catch_warnings():
    warnings.simplefilter("ignore", ReadyAPIDeprecationWarning)
    from examples.custom_response.tutorial001b_py310 import app

client = TestClient(app)


@pytest.mark.filterwarnings("ignore::readyapi.exceptions.ReadyAPIDeprecationWarning")
def test_get_custom_response():
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    assert response.json() == [{"item_id": "Foo"}]


@pytest.mark.filterwarnings("ignore::readyapi.exceptions.ReadyAPIDeprecationWarning")
def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == snapshot(
        {
            "openapi": "3.1.0",
            "info": {"title": "ReadyAPI", "version": "0.1.0"},
            "paths": {
                "/items/": {
                    "get": {
                        "responses": {
                            "200": {
                                "description": "Successful Response",
                                "content": {"application/json": {"schema": {}}},
                            }
                        },
                        "summary": "Read Items",
                        "operationId": "read_items_items__get",
                    }
                }
            },
        }
    )
