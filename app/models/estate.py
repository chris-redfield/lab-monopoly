from pydantic import BaseModel


class Estate(BaseModel):
    estate_id: int
    price: int
    rent: int
    owner: int = None
