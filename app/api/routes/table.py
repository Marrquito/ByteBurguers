from fastapi    import APIRouter, HTTPException, Response, status
from typing     import List

from api.controllers.table   import TableController
from api.requests.table import *
from api.responses.table import *


from datetime import datetime
import os
import logging

router = APIRouter()

logger          = logging.getLogger("ByteBurgers")

@router.post("/create", response_model=bool, status_code=status.HTTP_201_CREATED)
def tableCreate(table: TableRequestModel):
    controller  = TableController()
    
    newTable     = controller.create(table)

    if not newTable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Table not created"
        )
    
    return newTable

@router.put("/update/{id}", response_model=bool, status_code=status.HTTP_200_OK)
def tableUpdate(id:int, table: TableUpdateRequestModel):
    controller  = TableController()
    
    updateTable = controller.update(id, table)

    if not updateTable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Table not updated"
        )
    
    return updateTable

@router.get("/get/{id}", response_model=TableResponseModel, status_code=status.HTTP_200_OK)
def tableRead(id:int):
    controller  = TableController()
    
    getTable = controller.read(id)

    if not getTable:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Table not found"
        )
    
    return getTable

@router.delete("/delete/{id}", response_model=bool, status_code=status.HTTP_200_OK)
def tableDelete(id:int):
    controller  = TableController()
    
    deleteTable = controller.delete(id)

    if not deleteTable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Table not deleted"
        )

    return deleteTable