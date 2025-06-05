import uuid
from typing import Optional

from sqlalchemy.orm import Session

from app.model.todo import Todo
from app.schema.todo import TodoCreate, TodoUpdate


def get_by_id(db: Session, id: uuid.UUID) -> Optional[Todo]:
    return db.query(Todo).filter(Todo.id == id).first()


def create(db: Session, user_id: uuid.UUID, obj_in: TodoCreate) -> Todo:
    todo = Todo(
        user_id=user_id,
        title=obj_in.title,
        description=obj_in.description,
        due=obj_in.due
    )
    db.add(todo)
    db.flush()
    db.commit()
    return todo


def update(db: Session, id: uuid.UUID, obj_in: TodoUpdate) -> Optional[Todo]:
    todo = get_by_id(db, id)
    if not todo:
        return None
    todo.title = obj_in.title
    todo.description = obj_in.description
    todo.due = obj_in.due
    db.add(todo)
    db.flush()
    db.commit()
    return todo


def delete(db: Session, id: uuid.UUID) -> Optional[Todo]:
    todo = get_by_id(db, id)
    if not todo:
        return None
    db.delete(todo)
    db.flush()
    db.commit()
    return todo


def toggle_done(db: Session, id: uuid.UUID) -> Optional[Todo]:
    todo = get_by_id(db, id)
    if not todo:
        return None
    todo.is_done = not todo.is_done
    db.add(todo)
    db.flush()
    db.commit()
    return todo
