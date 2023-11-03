from pydantic import BaseModel

class ItemsOrderResponseModel(BaseModel):
    id              : int
    qtd             : int
    total_price     : float
    order_id        : int
    menu_id         : int

    class Config:
        from_attributes = True