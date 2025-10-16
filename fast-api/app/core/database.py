from pathlib import Path
from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel
from typing import Annotated, TypeAlias
from fastapi import Depends
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Place the sqlite file under a `database/` folder at the project root so it can be
# mounted into the container and accessed from the host (TablePlus).
BASE_DIR = Path(__file__).parent.parent.parent
DB_DIR = BASE_DIR / "database"
try:
    DB_DIR.mkdir(exist_ok=True)
    logger.info(f"✅ Database directory: {DB_DIR}")
except Exception as e:
    logger.error(f"❌ Cannot create database directory: {e}")
    DB_DIR = BASE_DIR
    logger.info("🔄 Using base directory for database")

DATABASE_URL = f"sqlite:///{DB_DIR/'user.db'}"
logger.info(f"📊 Database URL: {DATABASE_URL}")

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, connect_args=connect_args, echo=True)


def create_db_and_tables():
    try:
        SQLModel.metadata.create_all(engine)
        logger.info("✅ Database tables created successfully!")
    except Exception as e:
        logger.error(f"❌ Failed to create database tables: {e}")
        raise


def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()


SessionDep: TypeAlias = Annotated[Session, Depends(get_session)]