# Create Booking model
# Fields: user_id:int, room_id:int,nights:int(must be>=1),rate_per_nights:float
# Also add computed field:total_amount=nights*rate_per_night

from pydantic import BaseModel,Field,field_validator,model_validator,computed_field
from typing import Optional

class Booking(BaseModel):
    user_id:int
    room_id:int
    nights:int =Field(...,ge=1)
    rate_per_night:float

    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights*self.rate_per_night
    
