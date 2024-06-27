from fastapi import APIRouter
from users.schemas import SUser
from users.dao import UserDAO


router = APIRouter(prefix="/user", tags=["Пользователи"])

