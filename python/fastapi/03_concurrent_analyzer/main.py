import asyncio
from pathlib import Path
import time
from fastapi import FastAPI
from pydantic import BaseModel

class FilePath(BaseModel):
    path: Path

async def analyze_file(filepath: Path):
    # size = filepath.__sizeof__()
    try:
        size = filepath.stat().st_size
    except FileNotFoundError:
        size = 0
    print("scanning file for viruses....")
    await asyncio.sleep(2)
    return {"filename": f"{filepath.name}", "size": size}

app = FastAPI()


@app.post("/scan-all")
async def scan_all_files(files: list[FilePath]):
    start = time.time()
    task = [analyze_file(f.path) for f in files]
    result = await asyncio.gather(*task)

    return {"response": result, "time_taken": f"{time.time()-start:.2f} seconds"}


