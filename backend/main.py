# backend fastapi
# shows us that server works

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app=FastAPI(title=" RAG Chatbot")

@app.get("/")
def root():
    return {"message":"Chatbot backend is running"}

@app.get("/stream")
def start_stream():
    #stream response in chunks
    def fake_stream():
        messages = ["Hello", " from", " Agno", "!"]
        for msg in messages:
            yield msg
    return StreamingResponse(fake_stream(),media_type='text/plain')
