import logging

from sqlalchemy import select
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.db.session import get_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 1  # seconds
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def test_db() -> None:
    try:
        # Try to create session to check if DB is awake
        with get_db() as session:
            session.execute(select(1))
    except Exception as e:
        logger.error(e)
        raise e
