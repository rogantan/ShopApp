from pydantic import BaseModel, Field


class UserAddShema(BaseModel):
    name: str = Field(max_length=150)