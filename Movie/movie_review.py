'''Task: Design a Movie Schema
title -> string
director -> string
release_year -> integer
rating -> float (0 to 10)
genres -> list of strings
available -> boolean
duration -> integer (minutes)
language -> optional string

Validation rules:

title minimum 2 characters
director minimum 3 characters
release_year greater than 1900
rating between 0 and 10
duration greater than 0
genres should contain at least 1 genre '''

from pydantic import BaseModel,Field
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

movie=Movie(title='Harry Potter',
            director='Jonathon',
            release_year=2022,
            rating=8,
            genres=['comedy','action'],
            available=True,
            duration=180,
            language='English',
            reviews=[Review(username='Jake',comment='Awesome',stars=4),
                     Review(username='Ajita',comment='Mindblowing',stars=5)]
)
print(movie)