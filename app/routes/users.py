import logging
from fastapi import APIRouter, status, Request
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from fastapi.params import Depends
from app.dependencies import get_db_async
from app.services import user_service


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(
    request: Request,
    db: Annotated[AsyncSession, Depends(get_db_async)]
                      
                      
):
    body = await request.body()
    result = await user_service.create_user(body, db)

    
