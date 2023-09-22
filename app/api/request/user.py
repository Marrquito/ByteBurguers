from pydantic import BaseModel

class UserRequestModel(BaseModel):
    name        : str
    last_name   : str
    email       : str
    password    : str | None
    phone       : str

    class Config:
        from_attributes = True