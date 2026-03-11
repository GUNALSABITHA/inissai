from app.model import Posts


async def create_post(data:dict, db):
    new_post = Posts(
        title = data["title"],
        author_id = data["author_id"],
        content = data["content"],
    )
    db.add(new_post)
    await db.commit()


