from fastapi import Depends
from fastapi.routing import APIRouter
from db.db import get_session
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix="/images", tags=["Изображения"])