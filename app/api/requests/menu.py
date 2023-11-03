from pydantic   import BaseModel
from typing     import Optional

class MenuRequestModel(BaseModel):
    name        : str
    description : str
    cost        : float
    fabrication_place : str

    class Config:
        from_attributes = True