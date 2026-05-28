from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street:str
    city:str
    zip_code:int

class User(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool =True
    createdAt:datetime
    address:Address
    tags: List[str]=[]

    model_config=ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )

#create a user instance
user=User(
    id=1,
    name='Jake',
    email='jake01@gmail.com',
    is_active=True,
    createdAt=datetime(2024,2,12,4,2),
    address=Address(
        street='ktm',
        city='Kathmandu',
        zip_code=4401
    ),
    tags=['premium','subscriber']
)

# using model_dump() ->dict
python_dict=user.model_dump()

# using model_dump_json()
json_str=user.model_dump_json()
 
