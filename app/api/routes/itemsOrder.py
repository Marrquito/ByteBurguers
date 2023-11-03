from fastapi    import APIRouter, HTTPException, Response, status
from typing     import List

from api.controllers.itemsOrder   import *
from api.requests.itemsOrder import *
from api.responses.itemsOrder import *

from datetime import datetime
import os
import logging

router = APIRouter()

logger          = logging.getLogger("ByteBurgers")

@router.post("/create", response_model=bool, status_code=status.HTTP_201_CREATED)
def orderCreate(order: ItemsOrderRequestModel):
    controller = ItemsOrderController()
    
    newOrderEntry     = controller.create(order)

    if not newOrderEntry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Order entry not created"
        )
    
    return newOrderEntry

@router.get("/get/{id}", response_model=ItemsOrderResponseModel, status_code=status.HTTP_200_OK)
def orderRead(id:int):
    controller  = ItemsOrderController()
    
    getOrderEntry = controller.read(id)

    if not getOrderEntry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order entry not found"
        )
    
    return getOrderEntry

@router.put("/read_all/{id}", response_model=List[ItemsOrderResponseModel], status_code=status.HTTP_200_OK)
def orderReadAll(id:int):
    controller  = ItemsOrderController()
    
    getOrderEntry = controller.read_all(id)

    if not getOrderEntry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order entry not found"
        )
    
    return getOrderEntry

