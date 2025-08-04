from pydantic import BaseModel


class AddressAddShema(BaseModel):
    country: str
    city: str
    street: str
