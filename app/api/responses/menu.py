from pydantic import BaseModel

class MenuResponseModel(BaseModel):
    id                  : int
    name                : str
    description         : str
    cost                : float
    fabrication_place   : str
    qntd                : int

    class Config:
        from_attributes = True