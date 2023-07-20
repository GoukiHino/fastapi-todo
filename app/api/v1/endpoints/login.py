from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app import cruds, schemas
from app.api import deps
from app.core.security import create_access_token

router = APIRouter()


@router.post("/login", response_model=schemas.Token)
def login_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(deps.get_db)):
    user = cruds.user.authenticate(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": create_access_token(user.username), "token_type": "bearer"}
