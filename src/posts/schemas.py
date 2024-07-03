from pydantic import BaseModel


class SPost(BaseModel):
    text: str

