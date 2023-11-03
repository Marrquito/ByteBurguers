from pydantic import BaseModel
from datetime import datetime

class OrderResponseModel(BaseModel):
    id              : int
    date            : datetime
    total           : float
    payment_method  : str
    user_id         : int
    table_id        : int

    class Config:
        from_attributes = True