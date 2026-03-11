from pydantic import BaseModel, Field


def PostBase(BaseModel):
    title: str  = Field(min_length=2, alias = "title" )
    content: str = Field(min_length=2, alias = "content" )
    author_id = Field(alias = "userid")
    