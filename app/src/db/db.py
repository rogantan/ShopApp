from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
# from app.settings import settings
from sqlalchemy.ext.asyncio import AsyncSession
from db.base import Base

# DATABASE_URL = str(settings.db_url) # вручную свор
DATABASE_URL = "postgresql+asyncpg://postgres:yfhmzy03@127.0.0.1:5432/shop"
engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    async with async_session() as session:
        yield session

