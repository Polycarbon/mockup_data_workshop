from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, declarative_base

Base = declarative_base()


class Customer(Base):
    """Simple customer table with a handful of fields."""

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=True)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Customer id={self.id} name={self.name}>"
