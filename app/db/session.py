from contextlib import contextmanager
from typing import Generator

from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

SQLALCHEMY_DB_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(
    SQLALCHEMY_DB_URL,
    echo=settings.echo_sql,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@contextmanager
def get_db() -> Generator[Session, None, None]:
    """Returns a Generator to yield a session.

    Yields:
        Generator[Session, None, None]: Yields a session
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def get_db_dependency() -> Generator[Session, None, None]:
    """
    Dependency-Function for FastAPI-endpoints.
    """
    with get_db() as session:
        yield session


def get_db_metadata():
    metadata = MetaData()
    metadata.reflect(bind=engine)
    return metadata
