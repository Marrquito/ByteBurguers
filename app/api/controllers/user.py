import logging

from api.response.user      import UserResponseModel
from services.user_service  import UserService

logger = logging.getLogger("ByteBurgers")

class UserController():
    def __init__(self):
        logger.debug("UserController init")
        
    
    def listUsers(self) -> list[UserResponseModel]:
        logger.debug("[IN ] ListUsers")
        
        userService = UserService()
        
        result = userService.list()
        
        logger.debug(f"[OUT] - {result}")
