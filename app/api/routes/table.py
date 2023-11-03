from fastapi    import APIRouter, HTTPException, Response, status
from typing     import List

from api.controllers.table   import TableController
from api.requests.table import *


from datetime import datetime
import os
import logging

router = APIRouter()

logger          = logging.getLogger("ByteBurgers")

@router.post("/create", response_model=bool, status_code=status.HTTP_201_CREATED)
def tableCreate(table: TableRequestModel):
    controller  = TableController()
    
    newTable     = controller.create(table)
    
    return newTable

@router.put("/update/{id}", response_model=bool, status_code=status.HTTP_200_OK)
def tableUpdate(id:int, table: TableUpdateRequestModel):
    controller  = TableController()
    
    updateTable = controller.update(id, table)
    
    return updateTable

@router.delete("/delete/{id}", response_model=bool, status_code=status.HTTP_200_OK)
def tableDelete(id:int):
    controller  = TableController()
    
    deleteTable = controller.delete(id)
    
    return deleteTable