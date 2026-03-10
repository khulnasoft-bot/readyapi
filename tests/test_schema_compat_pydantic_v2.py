import enum

import pytest
from inline_snapshot import snapshot
from pydantic import BaseModel
from readyapi import ReadyAPI
from readyapi.testclient import TestClient

from tests.utils import needs_py310


@pytest.fixture(name="client")
def get_client():

    app = ReadyAPI()

    class PlatformRole(enum.StrEnum):
        admin = "admin"
        user = "user"

    class OtherRole(enum.StrEnum): ...

    class User(BaseModel):
        username: str
        role: PlatformRole | OtherRole

    @app.get("/users")
    async def get_user() -> User:
        return {"username": "alice", "role": "admin"}

    client = TestClient(app)
    return client


@needs_py310
def test_get(client: TestClient):
    response = client.get("/users")
    assert response.json() == {"username": "alice", "role": "admin"}


@needs_py310
def test_openapi_schema(client: TestClient):
    response = client.get("openapi.json")
    assert response.json() == snapshot(
        {
            "openapi": "3.1.0",
            "info": {"title": "ReadyAPI", "version": "0.1.0"},
            "paths": {
                "/users": {
                    "get": {
                        "summary": "Get User",
                        "operationId": "get_user_users_get",
                        "responses": {
                            "200": {
                                "description": "Successful Response",
                                "content": {
                                    "application/json": {
                                        "schema": {"$ref": "#/components/schemas/User"}
                                    }
                                },
                            }
                        },
                    }
                }
            },
            "components": {
                "schemas": {
                    "PlatformRole": {
                        "type": "string",
                        "enum": ["admin", "user"],
                        "title": "PlatformRole",
                    },
                    "User": {
                        "properties": {
                            "username": {"type": "string", "title": "Username"},
                            "role": {
                                "anyOf": [
                                    {"$ref": "#/components/schemas/PlatformRole"},
                                    {"enum": [], "title": "OtherRole"},
                                ],
                                "title": "Role",
                            },
                        },
                        "type": "object",
                        "required": ["username", "role"],
                        "title": "User",
                    },
                }
            },
        }
    )
