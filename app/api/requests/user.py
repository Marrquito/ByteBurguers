from pydantic   import BaseModel
from typing     import Optional

class UserRequestModel(BaseModel):
    name        : str
    last_name   : str
    email       : str
    password    : str | None
    phone       : str

    class Config:
        from_attributes = True

class UserUpdateRequestModel(BaseModel):
    name        : Optional[str] = None
    last_name   : Optional[str] = None
    email       : Optional[str] = None
    password    : Optional[str] = None
    phone       : Optional[str] = None

    class Config:
        from_attributes = True