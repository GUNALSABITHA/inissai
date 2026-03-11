from pydantic import BaseModel, Field


class UserBase(BaseModel):
    firstname: str = Field(min_length=2, alias = "firstName" )
    lastname: str = Field(min_length=2, alias = "secondName")
    
