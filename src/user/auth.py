from datetime import datetime, timedelta

from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from fastapi import Request
from sqlalchemy import update
from jose import jwt

from src.config import settings
from src.database import async_session_maker
from src.user.dao import UserDAO


from src.user.models import Users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)



async def authenticate_user(username : str , password : str):

    current = (await UserDAO.read(username=username))[0]
    print('!@!@' , current)
    if not current or not verify_password(password , current.password) :
        raise HTTPException(status_code=404)
    return current

def create_access_token(data : dict) -> str:

    to_copy = data.copy()
    expire_data = datetime.utcnow() + timedelta(1440)
    to_copy.update({"exp": expire_data})

    jwtt = jwt.encode(
        to_copy , settings.SECRET_KEY , settings.ALGORITHM
    )
    return jwtt


async def get_current_user(request: Request):

    token = request.cookies.get("booking_access_token")
    if token is None:
        raise HTTPException(status_code=404, detail={"отсутствует токен"}) from None

    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except:
        raise HTTPException(status_code=403, detail={"инвалидный токен"})

    user_id = decoded_token.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail={"отсутствует  такой пользователь"})

    user = await UserDAO.read(id=int(user_id))
    if not user:
        raise HTTPException(status_code=403, detail={"инвалидный пользователь"})
    return user[0]
