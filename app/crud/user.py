import uuid
from typing import Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.model.user import User
from app.schema.user import UserCreate


def get_by_id(db: Session, id: uuid.UUID) -> Optional[User]:
    return db.query(User).filter(User.id == id).first()


def get_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def create(db: Session, obj_in: UserCreate) -> User:
    user = User(
        username=obj_in.username,
        password=get_password_hash(obj_in.password)
    )
    db.add(user)
    db.flush()
    db.commit()
    return user


def delete(db: Session, id: uuid.UUID) -> Optional[User]:
    user = get_by_id(db, id)
    if not user:
        return None
    db.delete(user)
    db.flush()
    db.commit()
    return user


def authenticate(db: Session, username: str, password: str) -> Union[bool, User]:
    user = get_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
