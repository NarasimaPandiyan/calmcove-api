from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def process_messages(data: list):
    sender = []
    for message in data:
        role = message.get('role')
        content = message.get('content')
        sender.append(role)
        
    return {"message": str(sender)}
