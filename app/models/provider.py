from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String,Enum

from app.models.enums import AuthType
from app.db.base import Base
from datetime import datetime
from sqlalchemy.sql import func

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.endpoint import Endpoint
    from app.models.connection import Connection


class Provider(Base):
    __tablename__ = "providers"

    id: Mapped[int] = mapped_column(primary_key=True)

    name:Mapped[str]=mapped_column(String(100),nullable=False,unique=True)


    slug:Mapped[str]=mapped_column(String(100),nullable=False,unique=True)

    base_url: Mapped[str] = mapped_column(
            String(255),
            nullable=False
        )

    auth_type: Mapped[AuthType] = mapped_column(
        Enum(AuthType),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )
    connections:Mapped[list["Connection"]]=relationship("Connection",back_populates="provider")
    endpoints:Mapped[list["Endpoint"]]=relationship("Endpoint",back_populates="provider")