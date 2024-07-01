from fastapi import APIRouter
from posts.schemas import SPost, Update_post
from posts.dao import PostDAO



router = APIRouter(prefix="/posts", tags=["Посты"])

@router.get("/all_posts")
async def get_users():
    result = await PostDAO.get_posts()
    return result

@router.post("/add_post")   
async def add_post(post: SPost):                                
    await PostDAO.add_post(user_id=post.user_id, text=post.text)
    return "Пост запощен)"

@router.delete("/delete_post")
async def delete_post(post_id: int):                    
    await PostDAO.delete_post(post_id)
    return "Пост удален"

@router.patch("/update_post")                        
async def update_post(post: Update_post):
    await PostDAO.update_post(post.post_id, post.new_text)      
    return "Пост изменён"
