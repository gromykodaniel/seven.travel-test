import json

from fastapi import APIRouter, Depends, Response
from sqlalchemy import text
from src.database import async_session_maker

from src.user.auth import get_password_hash, authenticate_user, create_access_token, get_current_user

from src.user.dao import UserDAO
from fastapi import BackgroundTasks, FastAPI , HTTPException
router = APIRouter(prefix="", tags=["Контракты аутентификация"])



@router.post("/register", status_code=200)
#Как я понял пока без валидации почты (?)
async def register_user(username : str , password  :  str  ):

    existing_user = await UserDAO.read(username=username)
    if existing_user:  raise HTTPException(status_code=409 , detail={'Error': 'UserAlreadyExistsException'} )

    hashed_psw = get_password_hash(password)
    req = await UserDAO.create(username=username, password= hashed_psw)
    return req


@router.post("/login’", status_code=200)
async  def login_user(response: Response , username : str , password  :  str):

    user = await authenticate_user(username , password)
    new_token = create_access_token({'sub':str(user.id)})
    response.set_cookie("booking_access_token", new_token, httponly=True)
    return {'access_token':new_token}

@router.get("/user/me")
async def read_users_me(
        current_user = Depends(get_current_user)
):
    return current_user




#Потом уберу отсюда
@router.get("/ping", status_code=200)
async def PING_DB( ):


    async with async_session_maker() as session :
        try:
            await session.execute( text("SELECT 1") )
            print('LOG!1')
            return {'':'database are working'}
        except:return {'database':'not working'}

