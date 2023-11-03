from fastapi    import APIRouter, HTTPException, Response, status
from typing     import List

from api.controllers.menu   import MenuController
from api.requests.menu import *
from api.responses.menu import *


from datetime import datetime
import os
import logging

router = APIRouter()

logger          = logging.getLogger("ByteBurgers")

@router.post("/create", response_model=bool, status_code=status.HTTP_201_CREATED)
def menuCreate(menu: MenuRequestModel):
    controller = MenuController()
    
    newMenuEntry     = controller.create(menu)

    if not newMenuEntry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Menu entry not created"
        )
    
    return newMenuEntry
@router.put("/update/{id}", response_model=bool, status_code=status.HTTP_200_OK)
def menuUpdate(id:int, menu: MenuUpdateRequestModel):
    controller  = MenuController()
    
    updateMenuEntry = controller.update(id, menu)

    if not updateMenuEntry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Menu entry not updated"
        )
    
    return updateMenuEntry
@router.get("/get/{id}", response_model=MenuResponseModel, status_code=status.HTTP_200_OK)
def menuRead(id:int):
    controller  = MenuController()
    
    getMenuEntry = controller.read(id)

    if not getMenuEntry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu entry not found"
        )
    
    return getMenuEntry
@router.delete("/delete/{id}", response_model=bool, status_code=status.HTTP_200_OK)
def menuDelete(id:int):
    controller  = MenuController()
    
    deleteMenuEntry = controller.delete(id)

    if not deleteMenuEntry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Menu entry not deleted"
        )
    
    return deleteMenuEntry