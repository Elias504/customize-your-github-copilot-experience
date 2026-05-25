# Starter Code: Building REST APIs with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Mergington FastAPI Assignment")


class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True


# Simple in-memory store for this assignment.
items = []


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "FastAPI app is running"}


@app.post("/items")
def create_item(item: ItemCreate):
    """TODO: Add logic to assign an id and store the item."""
    pass


@app.get("/items")
def list_items():
    """TODO: Return all items."""
    pass


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """TODO: Return one item by id or raise 404."""
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemCreate):
    """TODO: Update an item by id or raise 404."""
    pass


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """TODO: Delete an item by id or raise 404."""
    pass


# Run with:
# uvicorn starter-code:app --reload
