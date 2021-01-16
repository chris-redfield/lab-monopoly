from typing import List, Optional
from pydantic import BaseModel, Field
from models.player import Player
from models.estate import Estate

class GameStateResponse(BaseModel):
    players_list: List[Player] = None
    players_order: List[Player]
    board: List[Estate]

class RunGameResponse(BaseModel):
    winner: Player
    round_: int