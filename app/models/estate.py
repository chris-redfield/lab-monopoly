from pydantic import BaseModel


class Estate(BaseModel):
    """ Propriedade, pode ser comprada e alugada. """
    estate_id: int
    price: int
    rent: int
    owner: int = None
