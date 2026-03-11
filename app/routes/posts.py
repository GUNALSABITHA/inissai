from fastapi import APIRouter, status, Request
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db_async
from fastapi.params import Depends
from app.services import post_service






router = APIRouter(prefix="/posts",tags=["Posts"])

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_post(
    request: Request,
    db: Annotated[AsyncSession, Depends(get_db_async)]
):
    
    body = await request.body()
    result = await post_service.create_post(body, db)
