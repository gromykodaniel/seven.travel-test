from fastapi import FastAPI

from src.tasks.router import router
from src.user.router import router as user_router
app = FastAPI()


app.include_router(router)
app.include_router(user_router)