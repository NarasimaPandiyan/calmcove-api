from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/v1/{Message}")
async def read_root(Message:str):
    return {"Hello": Message}