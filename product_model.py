# Create Product model with id,name,price,in_stock

from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str 
    price:float
    in_stock:bool =False

input_data={'id':101,'name':'Apple','price':9000,'in_stock':True}

product=Product(**input_data)
print(product)