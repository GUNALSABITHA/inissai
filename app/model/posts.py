from app.database import Base 
from sqlalchemy import Column, BigInteger, String, Text, DateTime, func, text, TIMESTAMP, ForeignKey
from datetime import datetime

from sqlalchemy.orm import relationship


class Posts(Base):
    __tablename__ = "posts"

    id = Column(BigInteger, primary_key = True, index = True)
    title = Column(Text)
    content  = Column(Text)

    author_id = Column(ForeignKey("users.id"))
    author = relationship("Users", back_populates="posts")

    created_at = Column(
        TIMESTAMP(timezone=True), 
        server_default=text("now()"),
        nullable=False,
        default=datetime.now,                        
                        )    
    last_updated_at = Column(
        TIMESTAMP(timezone=True),
        onupdate=datetime.now,
    )



