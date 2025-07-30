from fastapi.routing import APIRouter
from fastapi import Depends
from db.db import get_session
from sqlalchemy import select, update, insert
from user.models import Users
from sqlalchemy.ext.asyncio import AsyncSession
router = APIRouter(prefix="/users", tags=["Пользователи"])


@router.get("/get_users/{user_id}")
async def get_users(user_id: int):
    pass


@router.post("/add_users")
async def add_user(session: AsyncSession = Depends(get_session)):
    query = insert(Users).values(**{"name":"Andrey"})
    result = await session.execute(query)
    await session.commit()
    return {"message": "User is added"}

