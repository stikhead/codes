from fastapi import FastAPI, UploadFile, HTTPException
from pathlib import Path
from pydantic import BaseModel

# class logFile(BaseModel):
#     file: UploadFile
# is this even possibl lol
app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile):
    if not file.content_type.startswith("text/"):
        raise HTTPException(
            status_code=400,
            detail=f"invalid file type: {file.content_type}."
        )
    
    curr_dir = Path.cwd()
    save_dir = curr_dir/"logs"
    save_dir.mkdir(parents=True, exist_ok=True)
    new_file = save_dir/f"server_log_{file.filename}"
    mem = await file.read()
    new_file.write_bytes(mem)
    text_content = mem.decode("utf-8").splitlines()
    error_count = mem.count(b"ERROR")
    error_list = [line for line in text_content if "ERROR" in line]

    # for line in text_content:
    #     yield line
    #     new_file.write_text(line)
    return {"filename": "server.log", "error_count": error_count, "errorlist": error_list}

