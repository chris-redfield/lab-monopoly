from pydantic import BaseModel

class Estate(BaseModel):
    estate_id: int
    price:int # = $60 to $400
    rent: int # = $10 to $60
    owner: int = None