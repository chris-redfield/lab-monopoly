from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from models.player import Player, PlayerType
from models.estate import Estate

class GameStateResponse(BaseModel):
    players_list: List[Player] = None
    players_order: List[Player]
    board: List[Estate]

class RunGameResponse(BaseModel):
    winner: Player
    round_: int

class RunGamesResponse(BaseModel):
    n_timeout: int
    mean_rounds: int
    victory_percentage: Dict[str, int]
    top_type: PlayerType