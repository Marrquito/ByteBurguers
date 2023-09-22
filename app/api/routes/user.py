from fastapi    import APIRouter
from typing     import List

from api.response.user      import UserResponseModel
from api.controllers.user   import UserController



router = APIRouter()


@router.get("/", response_model=List[UserResponseModel])
def userList() -> List[UserResponseModel]:
    controller = UserController()
    
    users = controller.listUsers()
    
    if not users:
        return []
    
    return [UserResponseModel(user) for user in users]
