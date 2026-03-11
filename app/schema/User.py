from pydantic import BaseModel, Field


class UserBase(BaseModel):
    firstname: str = Field(min_length=2, alias = "firstName" )
    lastname: str = Field(min_length=2, alias = "secondName")
    email: str = Field(min_length=2, alias = "email")
    phone: str = Field(min_length=2, alias = "phone")
    image: str = Field(min_length=2, alias = "image")
    role: str = Field(min_length=2, alias = "role")
    username: str = Field(min_length=2, alias = "username")

    
