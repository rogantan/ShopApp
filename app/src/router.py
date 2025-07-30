from fastapi.routing import APIRouter
from user.router import router as user_router
api_router = APIRouter(prefix="/v1")

api_router.include_router(router=user_router)