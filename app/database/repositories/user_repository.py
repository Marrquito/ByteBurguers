import logging

from database.dependencies  import get_db
from database.models.user   import UserDBModel
from api.response.user      import UserResponseModel

logger = logging.getLogger("ByteBurgers")

class UserRepository:
    def __init__(self):
        logger.debug("UserRepository Init")
        
    def list(self) -> list[UserResponseModel]:
        logger.debug("[IN ]")
        
        result = None
        
        try:
            db_generator    = get_db()
            db              = next(db_generator)
            
            result = db.query(UserDBModel).all()
            
        except Exception as e:
            db.rollback()
            
            logger.error(f"[ERR] List User DB error - {e}")
            
            raise e
            
        logger.debug(f"[OUT] - {result}")