from datetime import datetime
from pydantic import BaseModel


class URLSchema(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True
