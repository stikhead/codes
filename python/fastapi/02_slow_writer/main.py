from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from pathlib import Path

class LogEntry(BaseModel):
    filename: str
    content: str


app = FastAPI()

@app.post("/log/")
async def create_log(log: LogEntry):
    curr_dir = Path.cwd()
    log_dir = curr_dir/"log"
    log_dir.mkdir(parents=True, exist_ok=True)
    filename = log.filename
    new_file = log_dir/f"{filename}.txt"
    await asyncio.sleep(2)
    new_file.write_text(log.content)
    return {"status": "saved", "file": f"{filename}.txt"}


