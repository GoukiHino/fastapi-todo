from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app import cruds, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.TodoResponse)
def create(
        obj_in: schemas.TodoCreate,
        current_user: models.User = Depends(deps.get_current_user),
        db: Session = Depends(deps.get_db)
):
    return cruds.todo.create(current_user.id, obj_in, db)


@router.put("/{todo_id}", response_model=schemas.TodoResponse)
def update(
        todo_id: int,
        obj_in: schemas.TodoUpdate,
        current_user: models.User = Depends(deps.get_current_user),
        db: Session = Depends(deps.get_db)
):
    return cruds.todo.update(current_user.id, todo_id, obj_in, db)


@router.delete("/{todo_id}", response_model=schemas.TodoResponse)
def delete(
        todo_id: int,
        current_user: models.User = Depends(deps.get_current_user),
        db: Session = Depends(deps.get_db)
):
    return cruds.todo.delete(current_user.id, todo_id, db)


@router.put("/{todo_id}/toggle-completed", response_model=schemas.TodoResponse)
def toggle_completed(
        todo_id: int,
        current_user: models.User = Depends(deps.get_current_user),
        db: Session = Depends(deps.get_db)
):
    return cruds.todo.toggle_completed(current_user.id, todo_id, db)
