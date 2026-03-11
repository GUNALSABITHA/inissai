from app.database import Base
from sqlalchemy import Column, BigInteger, VARCHAR, Text, TEXT
from sqlalchemy.orm import relationship




class Users(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index = True)
    username = Column(VARCHAR(128), nullable=False)


    first_name = Column(VARCHAR(255), nullable=False)
    last_name = Column(VARCHAR(255), nullable=False)

    role = Column(VARCHAR(50), default="user")

    phone = Column(Text)
    email = Column(Text, nullable=False, unique=True)
    image = Column(TEXT)

