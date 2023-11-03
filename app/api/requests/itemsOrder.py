from pydantic   import BaseModel
from typing     import Optional

class ItemsOrderRequestModel(BaseModel):
    qtd             : int
    order_id        : int
    menu_id         : int

    class Config:
        from_attributes = True

class ItemsOrderUpdateRequestModel(BaseModel):
    qtd             : Optional[int] = None
    total_price     : Optional[float] = None
    order_id        : Optional[int] = None
    menu_id         : Optional[int] = None

    class Config:
        from_attributes = True