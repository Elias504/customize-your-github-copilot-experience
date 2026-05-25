# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Connect a FastAPI application to a SQLite database to persist data across restarts. You will practice database modeling, CRUD operations, and API integration with persistent storage.

## 📝 Tasks

### 🛠️ Set Up SQLite and Database Model

#### Description
Create a SQLite database connection and define an item model that will be stored in a table.

#### Requirements
Completed program should:

- Configure a SQLite database file for the FastAPI project.
- Define a table/model for items with fields such as `id`, `name`, `price`, and `in_stock`.
- Create the table automatically when the application starts.

### 🛠️ Replace In-Memory CRUD with Database CRUD

#### Description
Update API endpoints so they read and write data from SQLite instead of an in-memory list.

#### Requirements
Completed program should:

- Implement `POST /items` to insert a new row into the database.
- Implement `GET /items` and `GET /items/{item_id}` to read from the database.
- Implement `PUT /items/{item_id}` and `DELETE /items/{item_id}` using database operations.
- Return a `404` response when an item ID does not exist.

### 🛠️ Test Persistence and Validation

#### Description
Verify request validation still works and confirm data remains available after restarting the server.

#### Requirements
Completed program should:

- Keep request validation with Pydantic models.
- Demonstrate at least one successful create/read flow.
- Restart the server and confirm previously created items still exist.
- Demonstrate one error case (for example, invalid input or missing item).
