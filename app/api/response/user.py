from pydantic import BaseModel

class UserResponseModel(BaseModel):
    id          : int
    name        : str
    last_name   : str
    email       : str
    phone       : str

    class Config:
        from_attributes = True