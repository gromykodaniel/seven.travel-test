from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.tasks.router import router
from src.user.router import router as user_router
app = FastAPI()


app.include_router(router)
app.include_router(user_router)



origins = [

    "*",


]

app.add_middleware(

    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
