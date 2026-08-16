from sqlalchemy import ForeignKey, String,UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.db.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.organization import Organization



class User(Base):
    __tablename__ = "users"
    __table_args__=(UniqueConstraint("email",name="uq_email"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"))
    organization: Mapped["Organization"] = relationship("Organization", back_populates="users")
    email:Mapped[str]=mapped_column(String(255),nullable=False)
    hashed_password:Mapped[str]=mapped_column(String(255),nullable=False)

