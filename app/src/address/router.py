from fastapi import Depends
from fastapi.routing import APIRouter
from db.db import get_session
from sqlalchemy import select, update, delete, insert
from address.models import Addresses
from sqlalchemy.ext.asyncio import AsyncSession
from address.shemas import AddressAddShema

router = APIRouter(prefix="/addresses", tags=["Адреса"])


@router.get("/get_addresses/{address_id}")
async def get_addresses(address_id: str, session: AsyncSession = Depends(get_session)):
    query = select(Addresses).where(id=address_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.post("/add_addresses")
async def add_address(address: AddressAddShema, session: AsyncSession = Depends(get_session)):
    query = insert(Addresses).values(**{"country": address.country, "city": address.city, "street": address.street})
    result = await session.execute(query)
    await session.commit()
    return {"message": "Address is added"}


@router.get("/get_addressess")
async def get_addresses(session: AsyncSession = Depends(get_session)):
    query = select(Addresses)
    result = await session.execute(query)
    return result.scalars().all()
