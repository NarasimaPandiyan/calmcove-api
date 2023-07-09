from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.post("/v1")
async def readData(data:list):
    return {"Hello": data}