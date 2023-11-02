from pydantic   import BaseModel
from typing     import Optional

class UserRequestModel(BaseModel):
    name        : str
    last_name   : str
    email       : str
    phone       : str
    city        : str
    watch_on    : bool
    is_flamengo : bool

    class Config:
        from_attributes = True

class UserUpdateRequestModel(BaseModel):
    name        : Optional[str]     = None
    last_name   : Optional[str]     = None
    email       : Optional[str]     = None
    phone       : Optional[str]     = None
    city        : Optional[str]     = None
    watch_on    : Optional[bool]    = None
    is_flamengo : Optional[bool]    = None

    class Config:
        from_attributes = True