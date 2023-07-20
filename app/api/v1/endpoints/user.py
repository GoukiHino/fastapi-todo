from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app import cruds, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.UserResponse)
def create(obj_in: schemas.UserCreate, db: Session = Depends(deps.get_db)):
    return cruds.user.create(obj_in, db)
