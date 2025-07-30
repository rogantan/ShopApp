from fastapi import FastAPI
from router import api_router as root_router
app = FastAPI()

app.include_router(root_router)