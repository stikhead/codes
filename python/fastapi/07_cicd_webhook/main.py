import asyncio
from fastapi import FastAPI, BackgroundTasks, HTTPException

from pydantic import BaseModel

class RepoLink(BaseModel):
    repo_link: str

async def build_docker_image(repo_name: str):
    print("starting build...")
    await asyncio.sleep(10)
    print("build complete!")


app = FastAPI()

@app.post("/webhook/")
async def build(repo: RepoLink,  bg_tasks: BackgroundTasks):
    if not repo.repo_link.startswith("https://"):
        raise HTTPException(
            status_code=400,
            detail=f"invalid repo link {repo.repo_link}"
        )
    
    bg_tasks.add_task(build_docker_image, repo.repo_link)
    return {"status": "accepted", "message": f"Docker build queued for {repo.repo_link}"} 

