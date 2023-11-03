from pydantic import BaseModel

class TableResponseModel(BaseModel):
    id              : int
    qntd_assentos   : int
    busy            : bool

    class Config:
        from_attributes = True