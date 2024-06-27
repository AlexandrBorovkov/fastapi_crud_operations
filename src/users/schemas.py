from pydantic import BaseModel, EmailStr


class SUser(BaseModel):
    name: str
    email: EmailStr
    password: str

