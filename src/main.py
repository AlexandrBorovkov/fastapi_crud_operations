from fastapi import FastAPI
import uvicorn

from users.router import router as router_users
from posts.router import router as router_posts


app = FastAPI()

app.include_router(router_users)
app.include_router(router_posts)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)