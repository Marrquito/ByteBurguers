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

@router.get("/read_all", response_model=List[MenuResponseModel], status_code=status.HTTP_200_OK)
def menuReadAll():
    controller  = MenuController()
    
    getMenuEntries = controller.read_all()

    if not getMenuEntries:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu entries not found"
        )
    
    return getMenuEntries

@router.get("/read_by_name", response_model=MenuResponseModel, status_code=status.HTTP_200_OK)
def menuReadByName(name:str):
    controller  = MenuController()
    
    getMenuEntries = controller.read_with_name(name)

    if not getMenuEntries:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu entries not found"
        )
    
    return getMenuEntries

@router.get("/read_by_fabrication_place", response_model=List[MenuResponseModel], status_code=status.HTTP_200_OK)
def menuReadByFabricationPlace(fabrication_place:str):
    controller  = MenuController()
    
    getMenuEntries = controller.read_by_fabrication_place(fabrication_place)

    if not getMenuEntries:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu entries not found"
        )
    
    return getMenuEntries

@router.get("/low_stock", response_model=List[MenuResponseModel], status_code=status.HTTP_200_OK)
def menuReadLowStock():
    controller  = MenuController()
    
    getMenuEntries = controller.read_low_stock()

    if not getMenuEntries:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu entries not found"
        )
    
    return getMenuEntries

@router.get("/read_by_cost", response_model=List[MenuResponseModel], status_code=status.HTTP_200_OK)
def menuReadByCost(minCost:float, maxCost:float):
    controller  = MenuController()
    
    getMenuEntries = controller.read_by_price_range(minCost, maxCost)

    if not getMenuEntries:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu entries not found"
        )
    
    return getMenuEntries

@router.delete("/delete/{id}", response_model=bool, status_code=status.HTTP_200_OK)
def menuDelete(id:int):
    controller  = MenuController()
    
    deleteMenuEntry = controller.delete(id)

    if not deleteMenuEntry:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Menu entry not deleted"
        )
    
    return deleteMenuEntry