from pydantic import BaseModel

class UserResponseModel(BaseModel):
    id          : int
    name        : str
    last_name   : str
    email       : str
    phone       : str
    city        : str
    watch_on    : bool
    is_flamengo : bool

    class Config:
        from_attributes = True