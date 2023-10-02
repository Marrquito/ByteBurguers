import logging

from api.responses.user      import UserResponseModel
from api.requests.user       import UserRequestModel
from services.user_service   import UserService

logger = logging.getLogger("ByteBurgers")

class UserController():
    def __init__(self):
        logger.debug("UserController init")
        
    
    def listUsers(self, name: str = None) -> list[UserResponseModel]:
        logger.debug("[IN ] ListUsers")
        
        userService = UserService()
        
        result      = userService.list(name)
        
        logger.debug(f"[OUT] - {result}")
        
        return result
  
    def createUser(self, user: UserRequestModel) -> UserResponseModel:
        logger.debug("[IN ] CreateUsers")
        
        userService = UserService()
        
        result      = userService.create(user)
        
        logger.debug(f"[OUT] - {result}")
        
        return result

    def readUser(self, id: int) -> UserResponseModel:
        logger.debug("[IN ] ReadUsers")
        
        userService = UserService()
        
        result      = userService.read(id)
        
        logger.debug(f"[OUT] - {result}")
        
        return result
 
    def updateUser(self, id: int, user: UserRequestModel) -> UserResponseModel:
        logger.debug("[IN ] UpdateUsers")
        
        userService = UserService()
        
        result      = userService.update(id, user)
        
        logger.debug(f"[OUT] - {result}")
        
        return result

    def deleteUser(self, id: int) -> bool:
        logger.debug("[IN ] DeleteUsers")
        
        userService = UserService()
        
        result      = userService.delete(id)
        
        logger.debug(f"[OUT] - {result}")
        
        return result
    
    def countUsers(self) -> int:
        logger.debug("[IN ] CountUsers")
        
        userService = UserService()
        
        result      = userService.count()
        
        logger.debug(f"[OUT] - {result}")
        
        return result
