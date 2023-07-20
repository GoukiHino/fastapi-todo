import datetime

from jose import jwt

from passlib.context import CryptContext

SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 60 * 24 * 7

pwd_context = CryptContext(schemes=["bcrypt"])


def create_access_token(sub: str) -> str:
    to_encode = {
        "sub": sub,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=EXPIRE_MINUTES)
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_hashed_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
