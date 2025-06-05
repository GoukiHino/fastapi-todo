import uuid

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app import crud, model, schema
from app.api.deps import get_db, get_current_user

router = APIRouter()


@router.post("/create", response_model=schema.TodoResponse)
def create(
        obj_in: schema.TodoCreate,
        db: Session = Depends(get_db),
        current_user: model.User = Depends(get_current_user)
):
    todo = crud.todo.create(db, current_user.id, obj_in)
    return todo


@router.put("/{id}/", response_model=schema.TodoResponse)
def update(id: uuid.UUID, obj_in: schema.TodoUpdate, db: Session = Depends(get_db)):
    return crud.todo.update(db, id, obj_in)


@router.delete("/{id}/delete", response_model=schema.TodoResponse)
def delete(id: uuid.UUID, db: Session = Depends(get_db)):
    return crud.todo.delete(db, id)


@router.put("/{id}/done", response_model=schema.TodoResponse)
def done(id: uuid.UUID, db: Session = Depends(get_db)):
    return crud.todo.toggle_done(db, id)
