from fastapi.routing import APIRouter
from fastapi import Depends
from db.db import get_session
from sqlalchemy import select, insert, update
from supplier.models import Suppliers
from sqlalchemy.ext.asyncio import AsyncSession
from supplier.shemas import SupplierAddShema

router = APIRouter(prefix="/suppliers", tags=["Поставщики"])


@router.get("/get_suppliers/{supplier_id}")
async def get_suppliers(supplier_id: str, session: AsyncSession = Depends(get_session)):
    query = select(Suppliers).filter_by(id=supplier_id)
    result = await session.execute(query)
    return result.scalars().first()


@router.post("/add_suppliers")
async def add_suppliers(supplier: SupplierAddShema, session: AsyncSession = Depends(get_session)):
    query = insert(Suppliers).values(**{"name": supplier.name, "address_id": supplier.address_id,
                                        "phone_number": supplier.phone_number})
    await session.execute(query)
    await session.commit()
    return {"message": "Supplier is added"}


@router.get("/get_suppliers")
async def get_suppliers(session: AsyncSession = Depends(get_session)):
    query = select(Suppliers)
    result = await session.execute(query)
    return result.scalars().all()