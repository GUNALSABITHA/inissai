from fastapi import FastAPI

from dotenv import load_dotenv

from app.database import init_models
from app.routes import  User_Router
from app.routes import  Post_Router

import logging


load_dotenv()
logger = logging.getLogger(__name__)

async def lifespan(app: FastAPI):   
    init_models()
    logger.debug("Models initialized successfully.")
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(User_Router)
app.include_router(Post_Router)


@app.post("/test")
def test():
    return {"message": "Hello World"}   




