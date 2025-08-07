from fastapi import Depends
from fastapi.routing import APIRouter
from db.db import get_session
from sqlalchemy import select, insert, delete
from product.models import Products
from sqlalchemy.ext.asyncio import AsyncSession
from product.shemas import ProductAddShema

router = APIRouter(prefix="/products", tags=["Товары"])


@router.post("/add_products")
async def add_products(product: ProductAddShema, session: AsyncSession = Depends(get_session)):
    query = insert(Products).values(**{"name": product.name, "category": product.category,
                                       "price": product.price, "available_stock": product.available_stock,
                                       "last_update_date": product.last_update_date, "supplier_id": product.supplier_id,
                                       "image_id": product.image_id})
    await session.execute(query)
    await session.commit()
    return {"message": "Product is added"}


@router.get("/get_products")
async def get_products(session: AsyncSession = Depends(get_session)):
    query = select(Products)
    result = await session.execute(query)
    return result.scalars().all()