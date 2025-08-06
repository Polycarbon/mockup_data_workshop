from __future__ import annotations

"""SQLAlchemy ORM models for the factory-based demo."""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from db import Base  # Use the shared declarative base from db.py


class Customer(Base):
    """Customer table for demonstration purposes."""

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=True)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Customer id={self.id} name={self.name}>"
