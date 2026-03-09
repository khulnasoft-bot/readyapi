from typing import Annotated

from readyapi import Depends, ReadyAPI
from readyapi.testclient import TestClient


async def some_value() -> int:
    return 123


type DependedValue = Annotated[int, Depends(some_value)]


def test_pep695_type_dependencies():
    app = ReadyAPI()

    @app.get("/")
    async def get_with_dep(value: DependedValue) -> str:  # noqa
        return f"value: {value}"

    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == '"value: 123"'
