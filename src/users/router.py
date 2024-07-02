from fastapi import APIRouter, Depends, HTTPException, Response, status
from users.schemas import SUser
from users.dao import UserDAO
from users.auth import authenticate_user, create_access_token, get_password_hash
from users.models import User
from exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from users.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"])


@router.post("/register")
async def register_user(user_data: SUser):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(name=user_data.name, email=user_data.email, hashed_password=hashed_password)

@router.post("/login")
async def login_user(response: Response, user_data: SUser):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("user_access_token", access_token, httponly=True)
    return access_token
    
@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("user_access_token")

@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
