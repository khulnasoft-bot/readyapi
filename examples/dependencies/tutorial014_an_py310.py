import time
from typing import Annotated

from readyapi import Depends, HTTPException, ReadyAPI
from readyapi.responses import StreamingResponse
from sqldev import Field, Session, SQLDev, create_engine

engine = create_engine("postgresql+psycopg://postgres:postgres@localhost/db")


class User(SQLDev, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


app = ReadyAPI()


def get_session():
    with Session(engine) as session:
        yield session


def get_user(user_id: int, session: Annotated[Session, Depends(get_session)]):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=403, detail="Not authorized")
    session.close()


def generate_stream(query: str):
    for ch in query:
        yield ch
        time.sleep(0.1)


@app.get("/generate", dependencies=[Depends(get_user)])
def generate(query: str):
    return StreamingResponse(content=generate_stream(query))
