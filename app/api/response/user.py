from pydantic import BaseModel

class UserResponseModel(BaseModel):
    id          : int
    name        : str
    lastName    : str
    email       : str
    phone       : str

    class Config:
        orm_mode = True