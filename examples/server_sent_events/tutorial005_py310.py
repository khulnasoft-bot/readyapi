from collections.abc import AsyncIterable

from pydantic import BaseModel
from readyapi import ReadyAPI
from readyapi.sse import EventSourceResponse, ServerSentEvent

app = ReadyAPI()


class Prompt(BaseModel):
    text: str


@app.post("/chat/stream", response_class=EventSourceResponse)
async def stream_chat(prompt: Prompt) -> AsyncIterable[ServerSentEvent]:
    words = prompt.text.split()
    for word in words:
        yield ServerSentEvent(data=word, event="token")
    yield ServerSentEvent(raw_data="[DONE]", event="done")
