from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

async def generator():
    words = ["#!/bin/bash\n", "echo 'Updating system...'\n", "apt-get update\n"]

    for word in words:
        yield word
        await asyncio.sleep(4)

app = FastAPI()

@app.get("/chat")
async def script():
    return StreamingResponse(generator(), media_type="text/event-stream")
