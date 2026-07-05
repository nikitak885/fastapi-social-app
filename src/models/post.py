
from pydantic import BaseModel


class UserPostIn(BaseModel):
    body:str 
    
class UserPost(BaseModel):
    id:int