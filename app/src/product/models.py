import uuid
from sqlalchemy import (
    ForeignKey,
    String,
    UUID,
    Date
)

from sqlalchemy import Column, Integer, Boolean, FLOAT, DECIMAL, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from db.base import Base


class Products(Base):
    __tablename__ = "Products"
    id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4())
    name: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(FLOAT, nullable=False)
    available_stock: Mapped[int] = mapped_column(Integer, nullable=False)
    last_update_date: Mapped[datetime] = mapped_column(Date, nullable=False)
    supplier_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("Suppliers.id"), nullable=False)
    image_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('Images.id'), nullable=False)