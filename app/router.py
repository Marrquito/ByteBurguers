from fastapi import APIRouter

from api.routes import user
from api.routes import table
from api.routes import menu
from api.routes import order
from api.routes import itemsOrder

router = APIRouter()

router.include_router(user.router, prefix="/user", tags=["User"])
router.include_router(table.router, prefix="/table", tags=["Table"])
router.include_router(menu.router, prefix="/menu", tags=["Menu"])
router.include_router(order.router, prefix="/order", tags=["Order"])
router.include_router(itemsOrder.router, prefix="/itemsOrder", tags=["ItemsOrder"])