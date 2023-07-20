from typing import Optional

from sqlalchemy.orm import Session

from app.core.security import create_hashed_password, verify_password
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def create(obj_in: UserCreate, db: Session) -> User:
    user = User(
        username=obj_in.username,
        password=create_hashed_password(obj_in.password),
        display_name=obj_in.display_name
    )
    db.add(user)
    db.commit()
    return user


def get(username: str, db: Session) -> Optional[User]:
    return db.query(User).filter(User.username == username, User.is_deleted == False).first()


def update(username: str, obj_in: UserUpdate, db: Session) -> User:
    user = get(username, db)
    if obj_in.password:
        user.password = create_hashed_password(obj_in.password)
    user.username = obj_in.username
    user.display_name = obj_in.display_name
    db.add(user)
    db.commit()
    return user


def delete(username: str, db: Session) -> User:
    user = get(username, db)
    user.is_deleted = True
    db.add(user)
    db.commit()
    return user


def authenticate(username: str, password: str, db: Session) -> Optional[User]:
    user = get(username, db)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
