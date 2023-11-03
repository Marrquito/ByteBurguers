from fastapi    import APIRouter, HTTPException, Response, status
from typing     import List

from api.controllers.menu   import MenuController
from api.requests.menu import *


from datetime import datetime
import os
import logging

router = APIRouter()

logger          = logging.getLogger("ByteBurgers")

@router.post("/create", response_model=bool, status_code=status.HTTP_201_CREATED)
def menuCreate(menu: MenuRequestModel):
    controller  = MenuController()
    
    newMenuEntry     = controller.create(menu)
    
    return newMenuEntry