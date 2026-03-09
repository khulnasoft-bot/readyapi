# Test security scheme at the top level, including OpenAPI
# Ref: https://github.com/khulnasoft/readyapi/discussions/14263
# Ref: https://github.com/khulnasoft/readyapi/issues/14271
from inline_snapshot import snapshot
from readyapi import Depends, ReadyAPI
from readyapi.security import HTTPBearer
from readyapi.testclient import TestClient

app = ReadyAPI()

bearer_scheme = HTTPBearer()


@app.get("/", dependencies=[Depends(bearer_scheme)])
async def get_root():
    return {"message": "Hello, World!"}


client = TestClient(app)


def test_get_root():
    response = client.get("/", headers={"Authorization": "Bearer token"})
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Hello, World!"}


def test_get_root_no_token():
    response = client.get("/")
    assert response.status_code == 401, response.text
    assert response.json() == {"detail": "Not authenticated"}


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == snapshot(
        {
            "openapi": "3.1.0",
            "info": {"title": "ReadyAPI", "version": "0.1.0"},
            "paths": {
                "/": {
                    "get": {
                        "summary": "Get Root",
                        "operationId": "get_root__get",
                        "responses": {
                            "200": {
                                "description": "Successful Response",
                                "content": {"application/json": {"schema": {}}},
                            }
                        },
                        "security": [{"HTTPBearer": []}],
                    }
                }
            },
            "components": {
                "securitySchemes": {"HTTPBearer": {"type": "http", "scheme": "bearer"}}
            },
        }
    )
