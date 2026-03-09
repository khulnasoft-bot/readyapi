from inline_snapshot import snapshot
from readyapi.testclient import TestClient

from examples.middleware.tutorial001_py310 import app

client = TestClient(app)


def test_response_headers():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert "X-Process-Time" in response.headers


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == snapshot(
        {
            "openapi": "3.1.0",
            "info": {
                "title": "ReadyAPI",
                "version": "0.1.0",
            },
            "paths": {},
        }
    )
