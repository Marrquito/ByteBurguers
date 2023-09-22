from fastapi    import APIRouter, HTTPException, Response, status
from typing     import List

from api.response.user      import UserResponseModel
from api.request.user       import UserRequestModel
from api.controllers.user   import UserController


router = APIRouter()


@router.get("/", response_model=List[UserResponseModel], status_code=status.HTTP_200_OK)
def userList() -> List[UserResponseModel]:
    controller = UserController()
    
    users = controller.listUsers()
    
    if not users:
        return []
    
    return users

@router.post("/", response_model=UserResponseModel, status_code=status.HTTP_201_CREATED)
def userCreate(user: UserRequestModel) -> UserResponseModel:
    controller = UserController()
    
    newUser = controller.createUser(user)
    
    return newUser

@router.get("/{id}", response_model=UserResponseModel, status_code=status.HTTP_200_OK)
def userRead(id: int) -> UserResponseModel:
    controller = UserController()
    
    user = controller.readUser(id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    
    return user

@router.put("/{id}", response_model=UserResponseModel, status_code=status.HTTP_200_OK)
def userUpdate(id: int, user: UserRequestModel) -> UserResponseModel:
    controller = UserController()
    
    user = controller.updateUser(id, user)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    
    return user

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def userDelete(id: int):
    controller = UserController()
    
    result = controller.deleteUser(id)
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
