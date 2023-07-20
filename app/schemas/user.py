from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from app.schemas.todo import TodoResponse


class UserBase(BaseModel):
    username: str
    display_name: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True
    )


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int
    is_deleted: bool

    todos: List[TodoResponse] = []
