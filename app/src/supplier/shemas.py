from pydantic import BaseModel


class SupplierAddShema(BaseModel):
    name: str
    address_id: str
    phone_number: str
