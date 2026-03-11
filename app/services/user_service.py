from app.schema import User
from app.model import *
from sqlalchemy.ext.asyncio import AsyncSession





async def create_user(data: dict, db:AsyncSession ):
    try:
        new_user = Users(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            phone=data["phone"],
            username=data["username"],
        )
        db.add(new_user)
        await db.commit()

        return new_user
    except Exception as e:
        await db.rollback()
        raise
