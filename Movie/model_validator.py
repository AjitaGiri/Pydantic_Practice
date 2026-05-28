from pydantic import BaseModel,Field,model_validator
from typing import List,Annotated,Optional
from datetime import datetime

class Review(BaseModel):
    username:str
    comment:str
    stars:Annotated[int,Field(ge=1,le=5)]

class Movie(BaseModel):
    title:Annotated[str,Field(...,min_length=2)]
    director:Annotated[str,Field(...,min_length=3)]
    release_year:Annotated[int,Field(gt=1900)]
    rating:Annotated[float,Field(ge=0,le=10)]
    genres:Annotated[List[str],Field(min_length=1)]
    available:bool
    duration:Annotated[int,Field(gt=0)]
    language:Optional[str] = None
    reviews:List[Review]

    @model_validator(mode='after')
    def check(self):
        if self.rating>8 and not self.available:
            raise ValueError('High rates movies must be available')
        
        if self.duration>150 and len(self.genres)<2:
            raise ValueError('the genres must be atleast two when movies longer than 150 minutes')
        
        current_year=datetime.now().year
        if self.release_year>current_year:
            raise ValueError('Release cant be in future')
        
        return self
