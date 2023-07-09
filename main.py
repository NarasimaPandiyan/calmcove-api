from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
async def read_root(Message:dict):
    return {"Hello": Message}