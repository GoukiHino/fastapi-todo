import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, UUID, String
from sqlalchemy.orm import Mapped

from app.db.base_class import Base


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[UUID] = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    user_id = Column(UUID, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    due = Column(DateTime)
    is_done = Column(Boolean, default=False)
