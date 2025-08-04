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
from address.models import Addresses


class Suppliers(Base):
    __tablename__ = 'Suppliers'
    id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    address_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('Addresses.id'), nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)

