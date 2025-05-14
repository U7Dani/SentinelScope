from sqlmodel import SQLModel, create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sentinelscope.db")
engine = create_engine(DATABASE_URL, echo=True)

async def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
