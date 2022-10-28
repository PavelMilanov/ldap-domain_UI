from pydantic import BaseModel
from datetime import datetime


class Customer(BaseModel):
    
    name: str
    lastlogoff: datetime
    lastlogon: datetime
