from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from jose import jwt

from app import cruds, models, schemas
from app.core.config import settings
from app.core.security import SECRET_KEY, ALGORITHM
from app.db.session import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_PREFIX}/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> models.User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = schemas.TokenPayload(**payload)
    except jwt.JWTError:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    user = cruds.user.get(token_data.sub, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
