from pydantic import BaseModel


class SPost(BaseModel):
    text: str

class SPost_update(BaseModel):
    post_id: int
    new_text: str
    