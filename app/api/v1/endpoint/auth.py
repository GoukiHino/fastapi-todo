from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app import crud, schema
from app.api.deps import get_db
from app.core.config import settings
from app.core.security import create_access_token

router = APIRouter()


@router.post("/login", response_model=schema.Token)
def login(response: Response, db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.username, form_data.password)
    user = crud.user.authenticate(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Invalid username or password"
        )
    access_token = create_access_token(user.username)
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        expires=settings.ACCESS_TOKEN_EXPIRE_SECONDS
    )
    return schema.Token(
        access_token=access_token,
        token_type="bearer"
    )
