from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app import cruds, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.UserResponse)
def create(
        obj_in: schemas.UserCreate,
        db: Session = Depends(deps.get_db)
):
    return cruds.user.create(obj_in, db)


@router.get("/me", response_model=schemas.UserResponse)
def get(
        current_user: models.User = Depends(deps.get_current_user)
):
    return current_user


@router.put("/me", response_model=schemas.UserResponse)
def update(
        obj_in: schemas.UserUpdate,
        current_user: models.User = Depends(deps.get_current_user),
        db: Session = Depends(deps.get_db)
):
    return cruds.user.update(current_user.username, obj_in, db)


@router.delete("/me", response_model=schemas.UserResponse)
def delete(
        current_user: models.User = Depends(deps.get_current_user),
        db: Session = Depends(deps.get_db)
):
    return cruds.user.delete(current_user.username, db)
