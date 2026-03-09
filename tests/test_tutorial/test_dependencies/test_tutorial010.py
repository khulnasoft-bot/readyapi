from typing import Annotated, Any
from unittest.mock import Mock, patch

from readyapi import Depends, ReadyAPI
from readyapi.testclient import TestClient

from examples.dependencies.tutorial010_py310 import get_db


def test_get_db():
    app = ReadyAPI()

    @app.get("/")
    def read_root(c: Annotated[Any, Depends(get_db)]):
        return {"c": str(c)}

    client = TestClient(app)

    dbsession_mock = Mock()

    with patch(
        "examples.dependencies.tutorial010_py310.DBSession",
        return_value=dbsession_mock,
        create=True,
    ):
        response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"c": str(dbsession_mock)}
