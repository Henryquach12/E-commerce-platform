from src.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from uuid import UUID, uuid4
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_name: Mapped[str] = mapped_column(String(50))
    full_name: Mapped[str] = mapped_column(String(100), nullable=True)
    phone_number: Mapped[str] = mapped_column(String, unique=True)
    address: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc))
    is_active: Mapped[bool] = mapped_column(default=True)
