import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# =========================
# Database URL
# =========================

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL environment variable is not configured"
    )


# =========================
# PostgreSQL Engine
# =========================

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


# =========================
# Session
# =========================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# =========================
# Base
# =========================

Base = declarative_base()