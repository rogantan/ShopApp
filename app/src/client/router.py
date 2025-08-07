from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException
from db.db import get_session
from sqlalchemy import select, update, insert, delete
from client.models import Clients
from sqlalchemy.ext.asyncio import AsyncSession
from client.shemas import ClientAddShema, ClientAddressShema
from address.models import Addresses
from uuid import UUID

router = APIRouter(prefix="/clients", tags=["Пользователи"])



@router.get("/get_clients/{client_id}")
async def get_clients(client_id: str, session: AsyncSession = Depends(get_session)):
    query = select(Clients).filter_by(id=client_id)
    result = await session.execute(query)
    return result.scalars().first()



@router.post("/add_clients")
async def add_clients(client: ClientAddShema, session: AsyncSession = Depends(get_session)):
    query = insert(Clients).values(**{"client_name":client.client_name, "client_surname": client.client_surname,
                                      "birthday": client.birthday, "gender": client.gender,
                                      "registration_date": client.registration_date, "address_id": client.address_id})
    result = await session.execute(query)
    await session.commit()
    return {"message": "Client is added"}


@router.get("/get_clients")
async def get_clients(session: AsyncSession = Depends(get_session)):
    query = select(Clients)
    result = await session.execute(query)
    return result.scalars().all()


@router.delete("/delete_clients/{client_id}")
async def delete_clients(client_id: str, session: AsyncSession = Depends(get_session)):
    query = delete(Clients).where(client_id == Clients.id)
    await session.execute(query)
    await session.commit()
    return {"message": "Client is deleted"}


@router.get("/get_clients_by_names")
async def get_clients_by_names(client_name: str, client_surname: str, session: AsyncSession = Depends(get_session)):
    query = select(Clients).where(client_name == Clients.client_name and client_surname == Clients.client_surname)
    result = await session.execute(query)
    response = []
    for row in result.scalars().all():
        response.append(
            ClientAddShema(
                client_name=row.client_name,
                client_surname=row.client_surname,
                birthday=row.birthday,
                gender=row.gender,
                registration_date=row.registration_date,
                address_id=row.address_id
            )
        )
    return response


@router.put("/update_client_addresses")
async def update_client_addresses(address: ClientAddressShema, session: AsyncSession = Depends(get_session)):
    try:
        query = insert(Addresses).values(**{"country": address.address.country, "city": address.address.city,
                                        "street": address.address.street}).returning(Addresses.id)
        result = await session.execute(query)
        a = result.scalar_one()
        if not a:
            raise HTTPException(500, detail="Error")
        query_1 = update(Clients).where(address.client_id == Clients.id).values(address_id=a)
        await session.execute(query_1)
        await session.commit()
        return 200
    except Exception as e:
        await session.rollback()
        return e


@router.get("/get_clients_with_pagination/")
async def get_clients_with_pagination(limit: int, offset: int, session: AsyncSession = Depends(get_session)):
    query = select(Clients).order_by(Clients.id).limit(limit).offset(offset)
    result = await session.execute(query)
    items = result.scalars().all()
    return {
        "limit": limit,
        "offset": offset,
        "count": len(items),
        "items": items
    }