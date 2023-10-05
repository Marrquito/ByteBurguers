from fastapi    import APIRouter, HTTPException, Response, status
from typing     import List

from api.responses.user      import UserResponseModel
from api.requests.user       import *
from api.controllers.user   import UserController

from datetime import datetime
import os
import logging

router = APIRouter()

logger          = logging.getLogger("ByteBurgers")

@router.get("/read_all", response_model=List[UserResponseModel], status_code=status.HTTP_200_OK)
def userList(name: str = None) -> List[UserResponseModel]:
    controller  = UserController()

    users       = controller.listUsers(name)
    
    if not users:
        return []
    
    return users

@router.post("/create", response_model=UserResponseModel, status_code=status.HTTP_201_CREATED)
def userCreate(user: UserRequestModel) -> UserResponseModel:
    controller  = UserController()
    
    newUser     = controller.createUser(user)
    
    return newUser

@router.get("/read/{id}", response_model=UserResponseModel, status_code=status.HTTP_200_OK)
def userRead(id: int) -> UserResponseModel:
    controller  = UserController()
    
    user        = controller.readUser(id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    
    return user

@router.put("/update/{id}", response_model=UserResponseModel, status_code=status.HTTP_200_OK)
def userUpdate(id: int, user: UserUpdateRequestModel) -> UserResponseModel:
    controller  = UserController()
    
    updateUser  = controller.updateUser(id, user)
    
    if not updateUser:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    
    return updateUser

@router.delete("/delete/{id}", status_code=status.HTTP_200_OK)
def userDelete(id: int):
    controller  = UserController()
    
    result      = controller.deleteUser(id)
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    
    return result

@router.get("/count", response_model=int, status_code=status.HTTP_200_OK)
def userCount() -> int:
    controller  = UserController()
    
    count       = controller.countUsers()
    
    return count

@router.get("/report", response_model=List[UserResponseModel], status_code=status.HTTP_200_OK)
def userReport() -> List[UserResponseModel]:
    controller  = UserController()
    
    count       = controller.countUsers()
    users       = controller.listUsers()

    dateNow     = datetime.now().strftime("%Y-%m-%d")

    reportName  = f"report_{dateNow}.txt"

    try:

        with open("relatorios/" + reportName, 'w') as arquivo:
            arquivo.write('Este é o relatório do dia ' + dateNow + '\n')
            arquivo.write('Quantidade de usuários: ' + str(count) + '\n')
            arquivo.write('Usuários:\n'+'id  - name - last_name - email - phone\n')
            for user in users:
                arquivo.write(f"{user.id} - {user.name} - {user.last_name} - {user.email} - {user.phone}\n")

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error generating report"
        )

    return users