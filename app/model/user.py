import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import Mapped, relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)

    todos = relationship("Todo", cascade="all, delete-orphan")
