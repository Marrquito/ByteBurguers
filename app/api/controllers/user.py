import logging

from api.response.user      import UserResponseModel
from api.request.user       import UserRequestModel
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
        
        return result
  
    def createUser(self, user: UserRequestModel) -> UserResponseModel:
        logger.debug("[IN ] ListUsers")
        
        userService = UserService()
        
        result = userService.create(user)
        
        logger.debug(f"[OUT] - {result}")
        
        return result

    def readUser(self, id: int) -> UserResponseModel:
        logger.debug("[IN ] ListUsers")
        
        userService = UserService()
        
        result = userService.read(id)
        
        logger.debug(f"[OUT] - {result}")
        
        return result
 
    def updateUser(self, id: int, user: UserRequestModel) -> UserResponseModel:
        logger.debug("[IN ] ListUsers")
        
        userService = UserService()
        
        result = userService.update(id, user)
        
        logger.debug(f"[OUT] - {result}")
        
        return result
