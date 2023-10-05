import logging

from sqlalchemy.sql import Select
from sqlalchemy.orm import Session

from database.dependencies  import get_db
from database.models.user   import UserDBModel
from api.responses.user     import UserResponseModel
from api.requests.user      import UserRequestModel

logger = logging.getLogger("ByteBurgers")

class UserRepository:
    def __init__(self):
        logger.debug("UserRepository Init")
        
    def list(self, name: str = None) -> list[UserResponseModel]:
        logger.debug("[IN ]")
        
        result = None
        
        try:
            db_generator    = get_db()
            db: Session     = next(db_generator)

            if name: 
                result = db.query(UserDBModel).filter(UserDBModel.name == name)
            else:
                result = db.query(UserDBModel).all()
            
        except Exception as e:
            db.rollback()
            
            logger.error(f"[ERR] List User DB error - {e}")
            
            raise e
        
        logger.debug(f"[OUT] - {result}")
            
        return result

    def count(self) -> int:
        logger.debug("[IN ]")
        
        result = None
        
        try:
            db_generator    = get_db()
            db: Session     = next(db_generator)
            
            result = db.query(UserDBModel).count()
            
        except Exception as e:
            db.rollback()
            
            logger.error(f"[ERR] Count User DB error - {e}")
            
            raise e
        
        logger.debug(f"[OUT] - {result}")
            
        return result

    def create(self, user: UserRequestModel) -> UserResponseModel:
        logger.debug("[IN ]")
        
        db_generator = get_db()
        db: Session  = next(db_generator)
        
        try:
            userDb = UserDBModel(**user.model_dump())
           
            db.add(userDb)
            db.commit()
            db.refresh(userDb)
            
        except Exception as e:
            db.rollback()
            
            logger.error(f"[ERR] Create User DB error - {e}")
            
            raise e
            
        logger.debug(f"[OUT] - {userDb}")
        
        return UserResponseModel(**userDb.__dict__)

    def read(self, id: int) -> UserResponseModel:
        logger.debug(f"[IN ] ID={id}")
        
        user = None
        
        db_generator = get_db()
        db: Session  = next(db_generator)
        
        try:
            user: UserResponseModel = db.query(UserDBModel).get(id)
            
        except Exception as e:
            db.rollback()
            
            logger.error(f"[ERR] Read User DB error - {e}")
            
            raise e
            
        logger.debug(f"[OUT] - {user}")
        
        return user

    def update(self, user: UserDBModel) -> UserResponseModel:
        logger.debug("[IN ]")
        
        db_generator = get_db()
        db: Session  = next(db_generator)
        
        updatedUser  = None
        
        try:
            updatedUser: UserResponseModel  = db.merge(user)
            
            db.commit()

        except Exception as e:
            db.rollback()
            
            logger.error(f"[ERR] Update User DB error - {e}")
            
            raise e
            
        logger.debug(f"[OUT] - {updatedUser}")
        
        return updatedUser

    def delete(self, id: int) -> bool:
        logger.debug("[IN ]")
        
        db_generator = get_db()
        db: Session  = next(db_generator)
        
        result = False
        
        try:
            user: UserResponseModel = db.query(UserDBModel).get(id)
            
            if user is not None:
                db.delete(user)
                db.commit()
                result = True
                

        except Exception as e:
            db.rollback()
            
            logger.error(f"[ERR] Delete User DB error - {e}")
            
            raise e
            
        logger.debug(f"[OUT] - {result}")
        
        return result