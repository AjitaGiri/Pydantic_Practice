# Create Employee model
#Fields: id:int, name:str (min 3chars), department:optional str (default 'General'), salary:float (must be >=10000)

from pydantic import BaseModel,Field 
from typing import List,Optional

class Employee(BaseModel):
    id:int
    name:str =Field(...,
                   min_length=3,
                   max_length=50,
                   description='Employee Name',
                   examples='Ajita Giri')
    department:Optional[str] ='General'
    salary:float = Field(...,
                         ge=10000)