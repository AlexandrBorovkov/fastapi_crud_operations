from database import async_session_maker
from sqlalchemy import select, insert
from posts.models import Post


class PostDAO:
    
    model = Post

    @classmethod
    async def get_posts(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def add_post(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_post(cls, post_id):
        async with async_session_maker() as session:
            query = select(cls.model).filter(cls.model.id == post_id)
            row = await session.execute(query)
            row = row.scalar_one()
            await session.delete(row)
            await session.commit()

    @classmethod
    async def update_post(cls, *args):
        async with async_session_maker() as session:
            post_id, new_text = args
            query = select(cls.model).filter(cls.model.id == post_id)
            row = await session.execute(query)
            row = row.scalar_one()
            row.text = new_text
            await session.commit()
