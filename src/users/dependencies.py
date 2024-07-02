from jose import jwt, JWTError

from datetime import datetime
from fastapi import Depends, Request


from config import settings
from exceptions import IncorrectTokenFormatException, TokenAbsentException, TokenExpiredException, UserIsNotPresentException
from users.dao import UserDAO


def get_token(request: Request):
    token = request.cookies.get("user_access_token")
    if not token:
        raise TokenAbsentException
    return token

async def get_current_user(token: str = Depends(get_token)):

    try:
        print(token)
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)

    except JWTError:
        raise IncorrectTokenFormatException
    
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UserDAO.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException

    return user