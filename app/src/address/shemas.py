from pydantic import BaseModel


# class AddressAddShema(BaseModel):
#     country: str
#     city: str
#     street: str


class AddressBaseShema(BaseModel):
    country: str
    city: str
    street: str


class AddressAddShema(AddressBaseShema):
    pass
