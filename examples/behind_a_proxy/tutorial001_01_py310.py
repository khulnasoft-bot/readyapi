from readyapi import ReadyAPI

app = ReadyAPI()


@app.get("/items/")
def read_items():
    return ["plumbus", "portal gun"]
