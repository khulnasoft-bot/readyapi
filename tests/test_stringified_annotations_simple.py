from __future__ import annotations

from typing import Annotated

from readyapi import Depends, ReadyAPI, Request
from readyapi.testclient import TestClient

from .utils import needs_py310


class Dep:
    def __call__(self, request: Request):
        return "test"


@needs_py310
def test_stringified_annotations():
    app = ReadyAPI()

    client = TestClient(app)

    @app.get("/test/")
    def call(test: Annotated[str, Depends(Dep())]):
        return {"test": test}

    response = client.get("/test")
    assert response.status_code == 200
