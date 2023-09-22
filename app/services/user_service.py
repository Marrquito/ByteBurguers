import logging

from database.repositories.user_repository  import UserRepository
from api.response.user                      import UserResponseModel
from api.request.user                       import UserRequestModel

logger = logging.getLogger("ByteBurgers")

class UserService:
    def __init__(self):
        logger.debug("User_Service init")
        
    def list(self) -> list[UserResponseModel]:
        logger.debug("List User service")
        
        result = []
        
        repository = UserRepository()
        
        result = repository.list()
        
        logger.debug(f"[OUT] - {result}")
        
        return result
        
    def create(self, user: UserRequestModel) -> UserResponseModel:
        logger.debug("List User service")
        
        repository = UserRepository()
        
        result = repository.create(user)
        
        logger.debug(f"[OUT] - {result}")
        
        return result

    def read(self, id: int) -> UserResponseModel:
        logger.debug("List User service")
        
        repository = UserRepository()
        
        result = repository.read(id)
        
        logger.debug(f"[OUT] - {result}")
        
        return result
    
    def update(self, id: int, user: UserRequestModel) -> UserResponseModel:
        logger.debug("List User service")
        
        repository = UserRepository()
        
        result = repository.update(id, user)
        
        logger.debug(f"[OUT] - {result}")
        
        return result
        
        