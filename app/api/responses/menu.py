from pydantic import BaseModel

class MenuResponseModel(BaseModel):
    id                  : int
    name                : str
    description         : str
    cost                : float
    fabrication_place   : str

    class Config:
        from_attributes = True