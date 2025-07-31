from fastapi.routing import APIRouter
from fastapi import Depends
from db.db import get_session
from sqlalchemy import select, update, insert
from user.models import Users
from sqlalchemy.ext.asyncio import AsyncSession
from user.shemas import UserAddShema

router = APIRouter(prefix="/users", tags=["Пользователи"])



@router.get("/get_users/{user_id}")
async def get_users(user_id: str, session: AsyncSession = Depends(get_session)):
    query = select(Users).filter_by(id=user_id)
    result = await session.execute(query)
    return result.scalars().first()



@router.post("/add_users")
async def add_user(user: UserAddShema, session: AsyncSession = Depends(get_session)):
    query = insert(Users).values(**{"name":user.name})
    result = await session.execute(query)
    await session.commit()
    return {"message": "User is added"}

