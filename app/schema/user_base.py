from pydantic import BaseModel


class UserBase(BaseModel):
    # id: uuid.UUID
    username: str
    # password: str
