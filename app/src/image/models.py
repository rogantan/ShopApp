import uuid
from sqlalchemy import (
    ForeignKey,
    String,
    UUID,
    LargeBinary
)
from sqlalchemy.orm import Mapped, mapped_column
from db.base import Base


class Images(Base):
    __tablename__ = "Images"
    id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4())
    image: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
