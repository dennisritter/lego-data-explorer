from app.db.models import Theme
from app.db.session import Session


class ThemeRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        themes = self.session.query(Theme).all()
        return themes

    def get_by_id(self):
        pass
