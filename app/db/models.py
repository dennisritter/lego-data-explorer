"Defines ORM-models for SQLAlchemy"

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship

Base = declarative_base()


class TimestampMixin:
    """Defines TimeStamp attributes for create and update."""

    @declared_attr
    def created_at(cls):
        return Column(DateTime, timezone=True, default=func.now(), nullable=False)

    @declared_attr
    def updaed_at(cls):
        return Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )


class Theme(Base, TimestampMixin):
    """Themes Database model."""

    __tablename__ = "themes"

    theme_id = Column(Integer, primary_key=True)
    theme_name = Column(String(256), nullable=False)
    parent_theme_id = Column(Integer, ForeignKey("themes.theme_id"), nullable=True)

    parent = relationship("Theme", back_populates="children")
    children = relationship("Theme", back_populates="parent")
