from fastapi import Depends
from fastapi.routing import APIRouter
from db.db import get_session
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from image.models import Images
from image.shemas import ImageShema, ImageAddShema


router = APIRouter(prefix="/images", tags=["Изображения"])


@router.post("/add_images")
async def add_images(image: ImageAddShema, session: AsyncSession = Depends(get_session)):
    query = insert(Images).values(**{"image": image.image})
    await session.execute(query)
    await session.commit()
    return {"message": "Images is added"}


@router.get("/get_images")
async def get_images(session: AsyncSession = Depends(get_session)):
    query = select(Images)
    result = await session.execute(query)
    response = []
    for image in result.scalars().all():
        response.append(
            ImageShema(
                id=image.id,
                image=image.image
            )
        )
    return response