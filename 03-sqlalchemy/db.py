from __future__ import annotations

"""SQLAlchemy utilities and Robot Framework keywords for the simple Customer demo.

This version does *not* require explicit session management keywords. A new
session is created for each operation and closed automatically, keeping the
Robot test scripts minimal.
"""

from pathlib import Path
import os
from typing import Any, Dict, Optional

from robot.api.deco import keyword  # type: ignore
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Customer  # noqa: E402  pylint: disable=wrong-import-position

# ---------------------------------------------------------------------------
# Engine and Session factory
# ---------------------------------------------------------------------------

DB_PATH = Path(__file__).parent.parent / "mock.db"
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Ensure tables exist at import time
Base.metadata.create_all(bind=engine)

# ---------------------------------------------------------------------------
# Robot Framework keywords
# ---------------------------------------------------------------------------

@keyword
def add_customer(name: str, email: str, phone: str | None = None) -> int:  # noqa: D401
    """Insert a customer and return its generated ID."""

    session = SessionLocal()
    try:
        cust = Customer(name=name, email=email, phone=phone)
        session.add(cust)
        session.commit()
        session.refresh(cust)
        return int(cust.id)
    finally:
        session.close()


@keyword
def get_customer_by_email(email: str) -> Optional[Dict[str, Any]]:  # noqa: D401
    """Fetch a customer by email. Returns a dict or ``None``."""

    session = SessionLocal()
    try:
        cust = session.query(Customer).filter(Customer.email == email).one_or_none()
        if cust is None:
            return None
        return {
            "id": cust.id,
            "name": cust.name,
            "email": cust.email,
            "phone": cust.phone,
        }
    finally:
        session.close()


@keyword
def delete_customer_by_email(email: str) -> int:  # noqa: D401
    """Delete customer(s) by email. Returns number of rows deleted."""

    session = SessionLocal()
    try:
        count = session.query(Customer).filter(Customer.email == email).delete()
        session.commit()
        return int(count)
    finally:
        session.close()
