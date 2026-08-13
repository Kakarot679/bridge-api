from sqlalchemy import Enum, String, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.db.base import Base
from datetime import datetime
from app.models.enums import ConnectionStatus

from typing import TYPE_CHECKING

if TYPE_CHECKING: 
    from app.models.organization import Organization
    from app.models.provider import Provider


class Connection(Base):
    __tablename__="connections"
    __table_args__=(UniqueConstraint("organization_id","provider_id",name="uq_connection_org_provider"),)


    id:Mapped[int]=mapped_column(primary_key=True)
    organization_id:Mapped[int]=mapped_column(ForeignKey("organizations.id",ondelete="CASCADE",name="fk_connections_organization_id"),nullable=False)
    provider_id:Mapped[int]=mapped_column(ForeignKey("providers.id",ondelete="CASCADE",name="fk_connections_provider_id"),nullable=False)
    access_token:Mapped[str]=mapped_column(Text,nullable=False)
    refresh_token:Mapped[str|None]=mapped_column(Text,nullable=True)
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())
    status:Mapped[ConnectionStatus]=mapped_column(Enum(ConnectionStatus),nullable=False,default=ConnectionStatus.ACTIVE)
    expires_at:Mapped[datetime|None]=mapped_column(nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
    server_default=func.now(),
    onupdate=func.now(),
    nullable=False
)
    organization:Mapped["Organization"]=relationship("Organization",back_populates="connections")
    provider:Mapped["Provider"]=relationship("Provider",back_populates="connections")
    