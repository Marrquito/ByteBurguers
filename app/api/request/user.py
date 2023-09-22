from pydantic import BaseModel, Field

class UserResponseModel(BaseModel):
    name        : str
    lastName    : str
    email       : str
    password    : str
    phone       : str

    class Config:
        orm_mode = True