import uuid
from typing import List

from pydantic import ConfigDict

from app.schema.user_base import UserBase
from app.schema.todo import TodoResponse


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id: uuid.UUID
    todos: List[TodoResponse] = []

    model_config = ConfigDict(
        from_attributes=True
    )
