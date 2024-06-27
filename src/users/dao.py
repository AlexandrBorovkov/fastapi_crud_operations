from database import async_session_maker
from sqlalchemy import select, insert
from users.models import User


class UserDAO:
    
    model = User

    


