import uuid
from sqlalchemy import (
    ForeignKey,
    String,
    UUID
)
#
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, DECIMAL, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
#
from db.base import Base


class Users(Base):
    __tablename__ = 'Users'
    id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)




# # class SubscriptionTypes(Base):
# #     __tablename__ = 'SubscriptionTypes'
# #     id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
# #     name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
# #
# #     users = relationship("Users", back_populates="subscription_type")
# #
# #
# # class Users(Base):
# #     __tablename__ = 'Users'
# #     id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
# #     username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
# #     password: Mapped[BYTEA] = mapped_column(type_=BYTEA(1024))
# #     role_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('Roles.id'), nullable=False)
# #     subscription_type_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('SubscriptionTypes.id'), nullable=False)
# #     is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default='true')
# #
# #     role = relationship("Roles", back_populates="users")
# #     subscription_type = relationship("SubscriptionTypes", back_populates="users")
# #     trades = relationship("Trade", back_populates="user")
# #     settings = relationship("Settings", back_populates="user")
# #     strategies = relationship("Strategy", back_populates="user")
# #
# #
# # class Direction(Base):
# #     __tablename__ = 'Direction'
# #     id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
# #     name: Mapped[str] = mapped_column(String, nullable=False)
# #
# #     trades = relationship("Trade", back_populates="direction")
# #
# #
# # class Instrument(Base):
# #     __tablename__ = 'Instrument'
# #     id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
# #     name: Mapped[str] = mapped_column(String, nullable=False)
# #
# #     tickers = relationship("Ticker", back_populates="instrument")
# #
# #
# # class Strategy(Base):
# #     __tablename__ = 'Strategy'
# #     id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
# #     name: Mapped[str] = mapped_column(String, nullable=False)
# #     user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('Users.id'), nullable=False)
# #     description: Mapped[str] = mapped_column(String)
# #     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False, server_default=func.now())
# #     updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False, server_default=func.now())
# #
# #     trades = relationship("Trade", back_populates="strategy")
# #     user = relationship("Users", back_populates="strategies")
# #
# #
# # class Ticker(Base):
# #     __tablename__ = 'Ticker'
# #     id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
# #     ticker: Mapped[str] = mapped_column(String)
# #     instrument_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('Instrument.id'), nullable=False)
# #     go: Mapped[DECIMAL] = mapped_column(DECIMAL)
# #     priceStep: Mapped[DECIMAL] = mapped_column(DECIMAL)
# #     priceStepValue: Mapped[DECIMAL] = mapped_column(DECIMAL)
# #     lot_size: Mapped[int] = mapped_column(Integer)
# #     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False, server_default=func.now())
# #     updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False, server_default=func.now())
# #
# #     instrument = relationship("Instrument", back_populates="tickers")
# #     trades = relationship("Trade", back_populates="ticker")
