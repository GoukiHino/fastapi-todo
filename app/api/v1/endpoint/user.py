from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app import crud, model, schema
from app.api.deps import get_db, get_current_user

router = APIRouter()


@router.get("/me", response_model=schema.UserResponse)
def get_me(current_user: model.User = Depends(get_current_user)):
    return current_user


@router.post("/create", response_model=schema.UserResponse)
def create(obj_in: schema.UserCreate, db: Session = Depends(get_db)):
    return crud.user.create(db, obj_in)


@router.delete("/delete", response_model=schema.UserResponse)
def delete_me(db: Session = Depends(get_db), current_user: model.User = Depends(get_current_user)):
    return crud.user.delete(db, current_user.id)
