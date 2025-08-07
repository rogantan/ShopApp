from pydantic import BaseModel
import uuid


class ImageAddShema(BaseModel):
    image: bytes


class ImageShema(BaseModel):
    id: uuid.UUID
    image: bytes