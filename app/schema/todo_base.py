import datetime
from typing import Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    # id: uuid.UUID
    # user_id: uuid.UUID
    title: str
    description: Optional[str] = None
    due: Optional[datetime.datetime] = None
    # is_done: bool
