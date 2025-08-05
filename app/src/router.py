from fastapi.routing import APIRouter
from client.router import router as client_router
from address.router import router as address_router
from supplier.router import router as supplier_router

api_router = APIRouter(prefix="/v1")

api_router.include_router(router=client_router)
api_router.include_router(router=address_router)
api_router.include_router(router=supplier_router)