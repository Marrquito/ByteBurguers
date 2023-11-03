from fastapi    import APIRouter, HTTPException, Response, status
from typing     import List

from api.controllers.order   import *
from api.requests.order import *
from api.responses.order import *

from datetime import datetime
import os
import logging

router = APIRouter()

logger          = logging.getLogger("ByteBurgers")

@router.post("/create", response_model=bool, status_code=status.HTTP_201_CREATED)
def orderCreate(order: OrderRequestModel):
    controller = OrderController()
    
    newOrderEntry     = controller.create(order)

    if not newOrderEntry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Order entry not created"
        )
    
    return newOrderEntry

@router.get("/get/{id}", response_model=OrderResponseModel, status_code=status.HTTP_200_OK)
def orderRead(id:int):
    controller  = OrderController()
    
    getOrderEntry = controller.read(id)

    if not getOrderEntry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order entry not found"
        )
    
    return getOrderEntry

@router.put("/update/{id}", response_model=bool, status_code=status.HTTP_200_OK)
def orderUpdate(id:int, order: OrderUpdateRequestModel):
    controller  = OrderController()
    
    updateOrderEntry = controller.update(id, order)

    if not updateOrderEntry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Order entry not updated"
        )
    
    return updateOrderEntry

@router.delete("/delete/{id}", response_model=bool, status_code=status.HTTP_200_OK)
def orderDelete(id:int):
    controller  = OrderController()
    
    deleteOrderEntry = controller.delete(id)

    if not deleteOrderEntry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Order entry not deleted"
        )
    
    return deleteOrderEntry

@router.put("/close_order/{id}", response_model=bool, status_code=status.HTTP_200_OK)
def orderClose(id:int, order: OrderUpdateRequestModel):
    controller  = OrderController()
    
    closeOrderEntry = controller.close_order(id, order)

    if not closeOrderEntry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Order entry not closed"
        )
    
    return closeOrderEntry