from readyapi import ReadyAPI
from readyapi.responses import HTMLResponse

app = ReadyAPI(default_response_class=HTMLResponse)


@app.get("/items/")
async def read_items():
    return "<h1>Items</h1><p>This is a list of items.</p>"
