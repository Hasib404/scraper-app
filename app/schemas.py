from pydantic import BaseModel


class URLSchema(BaseModel):
    url: str

    class Config:
        orm_mode = True
