from app.model import *
from sqlalchemy.ext.asyncio import AsyncSession





async def create_user(data: dict, db:AsyncSession ):
    try:
        new_user = Users(
            first_name=data.firstname,
            last_name=data.lastname,
            email=data.email,
            phone=data.phone,
            username=data.username,
            image=data.image,
            
        )
        db.add(new_user)
        await db.commit()
        
        return new_user
    except Exception as e:
        await db.rollback()
        raise
