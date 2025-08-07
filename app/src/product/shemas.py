from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class ProductAddShema(BaseModel):
    name: str
    category: str
    price: float
    available_stock: int
    last_update_date: datetime
    supplier_id: UUID
    image_id: UUID


