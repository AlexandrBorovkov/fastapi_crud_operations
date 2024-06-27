from pydantic import BaseModel


class SPost(BaseModel):
    user_id: int
    text: str

class Update_post(BaseModel):
    post_id: int
    new_text: str
    