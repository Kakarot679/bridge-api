from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.models.user import User
from app.models.connection import Connection


from app.db.base import Base

class Organization(Base):
    __tablename__="organizations"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(255),nullable=False)
    slug:Mapped[str]=mapped_column(String(100),nullable=False,unique=True)

    created_at:Mapped[datetime]=mapped_column(server_default=func.now())
    users:Mapped[list["User"]]=relationship("User",back_populates="organization",cascade="all, delete-orphan")
    connections:Mapped[list["Connection"]]=relationship("Connection",back_populates="organization")
