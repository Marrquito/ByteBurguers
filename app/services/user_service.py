import logging

from database.models.models                 import UserDBModel
from database.repositories.user_repository  import UserRepository
from api.responses.user                     import UserResponseModel
from api.requests.user                      import *

logger = logging.getLogger("ByteBurgers")

class UserService:
    def __init__(self):
        logger.debug("User_Service init")
        
    def list(self, name: str = None) -> list[UserResponseModel]:
        logger.debug("List User service")
        
        result      = []
        
        repository  = UserRepository()  
        
        result      = repository.list(name)
        
        logger.debug(f"[OUT] - {result}")
        
        return result
        
    def create(self, user: UserRequestModel) -> UserResponseModel:
        logger.debug("Create User service")
        
        repository   = UserRepository()
        
        result       = repository.create(user)
        
        logger.debug(f"[OUT] - {result}")
        
        return result

    def read(self, id: int) -> UserResponseModel:
        logger.debug(f"Read User service {id}")
        
        repository  = UserRepository()
        
        result      = repository.read(id)
        
        logger.debug(f"[OUT] - {result}")
        
        return result
    
    def update(self, id: int, user: UserUpdateRequestModel) -> UserResponseModel:
        logger.debug("Update User service")
        
        repository = UserRepository()
        
        try:
            updateUser  = UserDBModel(id = id, **user.model_dump(exclude_unset=True))
            result      = repository.update(updateUser)
        except Exception as e:
            logger.error(f"Error updating user failed - {e}")
            return None
        
        logger.debug(f"[OUT] - {result}")
        
        return result

    def delete(self, id: int) -> bool:
        logger.debug("Delete User service")
        
        repository  = UserRepository()
        
        result      = repository.delete(id)
        
        logger.debug(f"[OUT] - {result}")
        
        return result
        
    def count(self) -> int:
        logger.debug("Count User service")
        
        repository  = UserRepository()
        
        result      = repository.count()
        
        logger.debug(f"[OUT] - {result}")
        
        return result