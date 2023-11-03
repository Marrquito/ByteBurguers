from pydantic   import BaseModel
from typing     import Optional
from datetime   import datetime

class OrderRequestModel(BaseModel):
    total  : float = 0.0
    payment_method : str
    user_id : int
    table_id: int

    class Config:
        from_attributes = True

class OrderUpdateRequestModel(BaseModel):
    date    : Optional[datetime] = datetime.now(tz=None)
    total   : Optional[float] = None
    payment_method : Optional[str] = None
    user_id : Optional[int] = None
    table_id: Optional[int] = None

    class Config:
        from_attributes = True