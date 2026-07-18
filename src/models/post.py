
from pydantic import BaseModel


class UserPostIn(BaseModel):
    body:str 
    
class UserPost(BaseModel):
    id:int
    body:str
    
class CommentIn(BaseModel):
    body:str
    post_id:int
    
class Comment(CommentIn):
    id:int

class UserPostWthComments(BaseModel):
    post:UserPost
    comments:list[Comment] 
 