from fastapi import FastAPI

app = FastAPI()

@app.get("/v1/{Message}")
async def process_messages(Message: string): 
    return {"message": Message}
