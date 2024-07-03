from fastapi import APIRouter, Depends
from exceptions import UserDoesNotHaveRights
from posts.schemas import SPost
from posts.dao import PostDAO
from users.dependencies import get_current_user
from users.models import User


router = APIRouter(prefix="/posts", tags=["Посты"])

@router.get("/all_posts")
async def get_users():
    result = await PostDAO.get_posts()
    return result

@router.post("/add_post")   
async def add_post(post: SPost, user: User = Depends(get_current_user)):                                
    await PostDAO.add_post(user_id=user.id, text=post.text)
    return "Пост запощен)"

@router.delete("/delete_post")                                                 
async def delete_post(post_id: int, user_id: int, user: User = Depends(get_current_user)):
    if user_id != user.id:
        raise UserDoesNotHaveRights      
    await PostDAO.delete_post(post_id)
    return "Пост удален"

@router.patch("/update_post")                                                    
async def update_post(post_id: int, user_id: int, new_text: str, user: User = Depends(get_current_user)):
    if user_id != user.id:
        raise UserDoesNotHaveRights 
    await PostDAO.update_post(post_id, new_text)      
    return "Пост изменён"

