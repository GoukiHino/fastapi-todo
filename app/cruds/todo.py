from typing import Optional

from sqlalchemy.orm import Session

from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


def create(user_id: int, obj_in: TodoCreate, db: Session) -> Todo:
    todo = Todo(
        user_id=user_id,
        title=obj_in.title,
        description=obj_in.description
    )
    db.add(todo)
    db.commit()
    return todo


def get(todo_id: int, db: Session) -> Optional[Todo]:
    return db.query(Todo).filter(Todo.id == todo_id).first()


def update(todo_id: int, obj_in: TodoUpdate, db: Session) -> Todo:
    todo = get(todo_id, db)
    todo.title = obj_in.title
    todo.description = obj_in.description
    db.add(todo)
    db.commit()
    return todo


def delete(todo_id: int, db: Session) -> Todo:
    todo = get(todo_id, db)
    db.delete(todo)
    db.commit()
    return todo


def toggle_completed(todo_id: int, db: Session) -> Todo:
    todo = get(todo_id, db)
    todo.is_completed = not todo.is_completed
    db.add(todo)
    db.commit()
    return todo
