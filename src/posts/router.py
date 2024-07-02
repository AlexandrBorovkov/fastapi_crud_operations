from fastapi import APIRouter, Depends
from posts.schemas import SPost, SPost_update
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

@router.delete("/delete_post")                                                  # Исправить
async def delete_post(post_id: int,user: User = Depends(get_current_user)):                    
    await PostDAO.delete_post(post_id)
    return "Пост удален"

@router.patch("/update_post")                                                    # Исправить
async def update_post(post: SPost_update, user: User = Depends(get_current_user)):
    await PostDAO.update_post(post.post_id, post.new_text)      
    return "Пост изменён"
