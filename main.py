from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def process_messages(data: list):
    for message in data:
        role = message.get('role')
        content = message.get('content')
        # Process each message here based on the role and content
        
    return {"message": "Request processed successfully"}
