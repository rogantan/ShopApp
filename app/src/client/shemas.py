from pydantic import BaseModel, Field
from datetime import datetime
import uuid


class ClientAddShema(BaseModel):
    client_name: str = Field(max_length=150)
    client_surname: str = Field(max_length=150)
    birthday: datetime
    gender: str = Field(max_length=20)
    registration_date: datetime
    address_id: uuid.UUID


class ClientNameShema(BaseModel):
    client_name: str
    clint_surname: str


class ClientAddressShema(BaseModel):
    address_id: uuid.UUID