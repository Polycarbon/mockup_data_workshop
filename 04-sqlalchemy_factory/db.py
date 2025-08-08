from __future__ import annotations

"""SQLAlchemy utilities for the factory/ORM combo demo.

A simple engine and session factory are defined at import time – no explicit
session-management keywords are needed in Robot Framework.
"""

import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# ---------------------------------------------------------------------------
# Engine & Session factory
# ---------------------------------------------------------------------------

DB_PATH = Path(__file__).parent.parent / "mock.db"
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for models
Base = declarative_base()
