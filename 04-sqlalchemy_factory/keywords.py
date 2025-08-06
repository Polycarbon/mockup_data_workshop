from __future__ import annotations

"""Robot Framework library combining factory_boy and SQLAlchemy ORM."""

import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from robot.api.deco import keyword  # type: ignore

# Make sure this folder is importable despite the leading digits and hyphen.
current_dir = Path(__file__).parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

from db import SessionLocal  # noqa: E402  pylint: disable=wrong-import-position
from models import Customer  # noqa: E402  pylint: disable=wrong-import-position
from factories import CustomerFactory  # noqa: E402  pylint: disable=wrong-import-position


# ---------------------------------------------------------------------------
# Keyword implementations
# ---------------------------------------------------------------------------

@keyword
def create_fake_customers(count: int = 1) -> List[Dict[str, Any]]:  # noqa: D401
    """Generate *count* customers using the SQL-backed factory.

    Returns a list of customer dictionaries.
    """

    records = []
    if count is None:
        records.append(CustomerFactory())
    else:
        records.extend(CustomerFactory.create_batch(size=count))
    return records


@keyword
def get_customer_by_email(email: str) -> Optional[Dict[str, Any]]:  # noqa: D401
    """Fetch a customer by email, returning a dictionary or ``None``."""

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
    """Delete customers matching *email*. Returns number of rows removed."""

    session = SessionLocal()
    try:
        count = session.query(Customer).filter(Customer.email == email).delete()
        session.commit()
        return int(count)
    finally:
        session.close()
