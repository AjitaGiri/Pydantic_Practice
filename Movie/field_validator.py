''' Add validator in your Movie schema:

Director name should not contain numbers
Genre names should automatically become lowercase
'''
from pydantic import BaseModel,Field,field_validator
from typing import List,Annotated,Optional

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

#custom validation logic for fields
    @field_validator('genres')
    @classmethod
    def lower_value(cls,value):
        return [x.lower() for x in value] 
    
    @field_validator('director')
    @classmethod
    def no_number(cls,value):
      if any(char.isdigit() for char in value):
          raise ValueError("Username cannot contain numbers")
      return value
    
review=Review(username='Jake',comment='Awesome',stars=4)

input={'title':'Avengers',
       'director':'Jonathon',
       'release_year':2022,
       'rating':8,
       'genres':['comedy','action'],
       'available':True,'duration':180,
       'language':'English',
       'reviews':[review]
       }

movie=Movie(**input)
print(movie)