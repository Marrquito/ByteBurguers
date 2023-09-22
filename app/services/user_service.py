import logging

from database.repositories.user_repository  import UserRepository
from api.response.user                      import UserResponseModel

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
        
        