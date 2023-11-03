from pydantic   import BaseModel
from typing     import Optional

class MenuRequestModel(BaseModel):
    name        : str
    description : str
    cost        : float
    fabrication_place : str

    class Config:
        from_attributes = True

class MenuUpdateRequestModel(BaseModel):
    name        : Optional[str]      = None
    description : Optional[str]      = None
    cost        : Optional[float]    = None
    fabrication_place : Optional[str] = None

    class Config:
        from_attributes = True