# import statements
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Create FastAPI app
task = FastAPI()

# In-memory data storage
data_store = []
current_id = 1

# Request validation model
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

# Response models
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

class ItemListResponse(BaseModel):
    total_items: int
    items: List[ItemResponse]

# ----------------------------
# CREATE: Add new item
# ----------------------------
@task.post("/items", response_model=ItemResponse)
def create_item(item: Item):
    global current_id
    new_item = {
        "id": current_id,
        "name": item.name,
        "price": item.price,
        "description": item.description
    }
    data_store.append(new_item)
    current_id += 1
    return new_item

# ----------------------------
# READ: Get all items
# ----------------------------
@task.get("/items", response_model=ItemListResponse)
def get_all_items():
    return {
        "total_items": len(data_store),
        "items": data_store
    }

# ----------------------------
# READ: Get item by ID
# ----------------------------
@task.get("/items/{item_id}", response_model=ItemResponse)
def get_item_by_id(item_id: int):
    for item in data_store:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# ----------------------------
# UPDATE: Update item by ID
# ----------------------------
@task.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, updated_item: Item):
    for item in data_store:
        if item["id"] == item_id:
            item["name"] = updated_item.name
            item["price"] = updated_item.price
            item["description"] = updated_item.description
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# ----------------------------
# DELETE: Delete item by ID
# ----------------------------
@task.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(data_store):
        if item["id"] == item_id:
            data_store.pop(index)
            return {"message": f"Item {item_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
