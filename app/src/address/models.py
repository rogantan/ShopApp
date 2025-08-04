import uuid
from sqlalchemy import (
    ForeignKey,
    String,
    UUID,
    Date
)

from sqlalchemy import Column, Integer, Boolean, DECIMAL, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from db.base import Base


class Addresses(Base):
    __tablename__ = 'Addresses'
    id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    country: Mapped[str] = mapped_column(String, nullable=False)
    city: Mapped[str] = mapped_column(String, nullable=False)
    street: Mapped[str] = mapped_column(String, nullable=False)