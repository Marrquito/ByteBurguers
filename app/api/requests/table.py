from pydantic   import BaseModel
from typing     import Optional

class TableRequestModel(BaseModel):
    qntd_assentos   : int
    busy            : bool = False

    class Config:
        from_attributes = True

class TableUpdateRequestModel(BaseModel):
    qntd_assentos   : Optional[int]     = None
    busy            : Optional[bool]    = None

    class Config:
        from_attributes = True