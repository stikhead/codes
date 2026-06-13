from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
class AuthToken(BaseModel):
    token: str

def verify_admin(auth_header: AuthToken):
     
    if os.getenv('secret_key') != auth_header.token: 
        raise HTTPException(
            status_code=401, 
            detail="unauthorized"
        )
    
    return auth_header
    
    
    

@app.get("/ai-status", dependencies=[Depends(verify_admin)])
async def verify():
    return {"status": "Model is online and ready."}
    

    
    