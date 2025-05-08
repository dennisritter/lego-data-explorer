from sqlalchemy import literal_column, select

from app.db.session import get_db


def test_db() -> None:
    try:
        # Try to create session to check if DB is awake
        with get_db() as session:
            session.query(literal_column("current_user"))
            session.execute(select(1))
    except Exception as e:
        raise e
        raise e
