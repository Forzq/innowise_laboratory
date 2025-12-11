from pydantic import BaseModel
from typing import Optional

# for create
class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

# update
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None

# response
class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int]
    
    class Config:
        from_attributes = True