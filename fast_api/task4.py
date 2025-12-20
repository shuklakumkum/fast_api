#import statement
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# To create FastAPI app
task = FastAPI()

# Pydantic model
class User(BaseModel):
    name: str
    age: int
    email: str

# Fake database
users = []

# ---------------- CREATE ----------------
@task.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    users.append(user)
    return {
        "message": "User created successfully",
        "user_id": len(users) - 1
    }

# ---------------- READ ----------------
@task.get("/users")
def get_all_users():
    return users

@task.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return users[user_id]

# ---------------- UPDATE ----------------
@task.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: User):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    users[user_id] = user
    return {
        "message": "User updated successfully",
        "user": user
    }

# ---------------- DELETE ----------------
@task.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    deleted_user = users.pop(user_id)
    return {
        "message": "User deleted successfully",
        "deleted_user": deleted_user
    }
