"Defines ORM-models for SQLAlchemy"

from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import Mapped, mapped_column, relationship

Base = declarative_base()


class TimestampMixin:
    """Defines TimeStamp attributes for create and update."""

    @declared_attr
    def created_at(cls) -> Mapped[datetime]:
        return mapped_column(
            TIMESTAMP(timezone=True),
            server_default=func.now(),
            nullable=False,
        )

    @declared_attr
    def updated_at(cls) -> Mapped[datetime]:
        return mapped_column(
            TIMESTAMP(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )


class Theme(Base, TimestampMixin):
    """Themes Database model."""

    __tablename__ = "themes"

    theme_id: Mapped[int] = mapped_column(primary_key=True)
    theme_name: Mapped[str] = mapped_column(nullable=False)
    parent_theme_id: Mapped[int] = mapped_column(ForeignKey("themes.theme_id"), nullable=True)

    parent = relationship("Theme", back_populates="children")
    children = relationship("Theme", back_populates="parent")
