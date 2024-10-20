from fastapi import FastAPI
from app.routes import auth, users

app = FastAPI()


app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)

app.url_map.strict_slashes = False
