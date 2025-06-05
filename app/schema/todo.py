import uuid

from app.schema.todo_base import TodoBase


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class TodoResponse(TodoBase):
    id: uuid.UUID
    is_done: bool
