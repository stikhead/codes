# FastAPI is a web framework for building APIs. 
# It is incredibly fast because it is built entirely on asyncio under the hood.
# It also heavily utilizes Python's native type hints to automatically validate incoming data
# and generate beautiful documentation (Swagger UI) for your API for free.

# To run this, you would need to pip install fastapi uvicorn
# and run: uvicorn filename:app --reload

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# pydantic model automatically validate incoming json data
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# basic get endpoint

@app.get("/")
async def read_root():
    return {"message": "welcome to my fast api!"}

# get endpoint with a path parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "status": "Found"}

# post endpoint that expects json matching our pydantic model
@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"created {item.name}", "price_with_tax": item.price * 1.05}