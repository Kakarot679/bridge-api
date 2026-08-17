from sqlalchemy import String, ForeignKey,Enum
from sqlalchemy.orm import relationship,mapped_column, Mapped   
from sqlalchemy.sql import func
from app.models.enums import HttpMethod
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.provider import Provider

from app.db.base import Base

class Endpoint(Base):
    __tablename__ = "endpoints"

    id: Mapped[int] = mapped_column( primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    provider_id: Mapped[int] = mapped_column(ForeignKey("providers.id",ondelete="CASCADE",name="fk_endpoints_provider_id"),nullable=False)
    method:Mapped[HttpMethod]=mapped_column(Enum(HttpMethod),nullable=False)
    path: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str|None] = mapped_column(String(255), nullable=True)
    provider:Mapped["Provider"]=relationship("Provider",back_populates="endpoints")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())



