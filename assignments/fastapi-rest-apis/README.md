# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to create, read, update, and delete data. You will practice API route design, request validation, and structured JSON responses.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Set up a FastAPI application with a health-check route and an in-memory list to store items.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Add a `GET /health` endpoint that returns a JSON status message.
- Define an in-memory data store (for example, a list of dictionaries).

### 🛠️ Build CRUD Endpoints

#### Description
Implement endpoints to create, view, update, and delete items in your API.

#### Requirements
Completed program should:

- Add `POST /items` to create a new item.
- Add `GET /items` and `GET /items/{item_id}` to read items.
- Add `PUT /items/{item_id}` to update an item.
- Add `DELETE /items/{item_id}` to remove an item.
- Return appropriate HTTP status codes for success and not found cases.

### 🛠️ Add Validation and Test Requests

#### Description
Use Pydantic models for request validation and test your API endpoints.

#### Requirements
Completed program should:

- Define a Pydantic model for item input (for example: `name`, `price`, `in_stock`).
- Validate incoming request data using that model.
- Run the app with Uvicorn and test all routes.
- Demonstrate at least one successful response and one error response.
