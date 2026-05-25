# Starter Code: Persisting FastAPI Data with SQLite

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI SQLite Persistence Assignment")


class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True


class ItemResponse(ItemCreate):
    id: int


# TODO:
# 1. Add SQLite/SQLAlchemy setup.
# 2. Create a database model/table for items.
# 3. Initialize the database on startup.


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"}


@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate):
    """TODO: Insert into SQLite and return the created item."""
    raise HTTPException(status_code=501, detail="Not implemented")


@app.get("/items", response_model=list[ItemResponse])
def list_items():
    """TODO: Query and return all items from SQLite."""
    raise HTTPException(status_code=501, detail="Not implemented")


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    """TODO: Query item by id or return 404."""
    raise HTTPException(status_code=501, detail="Not implemented")


@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate):
    """TODO: Update existing item by id or return 404."""
    raise HTTPException(status_code=501, detail="Not implemented")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """TODO: Delete item by id or return 404."""
    raise HTTPException(status_code=501, detail="Not implemented")


# Run with:
# uvicorn starter-code:app --reload
