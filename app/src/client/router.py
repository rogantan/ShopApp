from fastapi.routing import APIRouter
from fastapi import Depends
from db.db import get_session
from sqlalchemy import select, update, insert
from client.models import Clients
from sqlalchemy.ext.asyncio import AsyncSession
from client.shemas import ClientAddShema

router = APIRouter(prefix="/clients", tags=["Пользователи"])



@router.get("/get_users/{user_id}")
async def get_users(user_id: str, session: AsyncSession = Depends(get_session)):
    query = select(Clients).filter_by(id=user_id)
    result = await session.execute(query)
    return result.scalars().first()



@router.post("/add_users")
async def add_user(user: ClientAddShema, session: AsyncSession = Depends(get_session)):
    query = insert(Clients).values(**{"name":user.name})
    result = await session.execute(query)
    await session.commit()
    return {"message": "User is added"}


@router.get("/get_users")
async def get_users(session: AsyncSession = Depends(get_session)):
    query = select(Clients)
    result = await session.execute(query)
    return result.scalars().all()

