import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

print(f"DATABASE_URL encontrada: {DATABASE_URL is not None}")

if not DATABASE_URL:
    raise RuntimeError("❌ DATABASE_URL no está configurada")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)