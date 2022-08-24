from datetime import datetime
from pydantic import BaseModel


class URLSchema(BaseModel):
    url: str
    created_at: datetime

    class Config:
        orm_mode = True
