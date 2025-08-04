from pydantic import BaseModel, Field
from datetime import datetime


class ClientAddShema(BaseModel):
    client_name: str = Field(max_length=150)
    client_surname: str = Field(max_length=150)
    birthday: datetime
    gender: str = Field(max_length=20)
    registration_date: datetime