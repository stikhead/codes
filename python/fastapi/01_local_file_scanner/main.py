from fastapi import FastAPI
from pathlib import Path
# from pydantic import BaseMode

app = FastAPI()

@app.get("/workspace")
async def get_files_names():
    curr_dir = Path.cwd()
    workspace = curr_dir/"workspace"

    if not workspace.exists():
        return {"error": "workspace folder not found."}
    

    file_name = [file.name for file in workspace.glob("*") if file.is_file]
    return {"files": file_name}



