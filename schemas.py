from pydantic import BaseModel
from typing import List

class CommentResponse(BaseModel):
    id: int
    content: str
    post_id: int

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    comments: List[CommentResponse] = []  # Embed comments

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    post_id: int
