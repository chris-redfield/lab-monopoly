from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from models.player import Player, PlayerType
from models.estate import Estate


class GameStateResponse(BaseModel):
    """Entidade response de inicialização de um jogo ou execução de uma rodada"""

    players_list: List[Player] = None
    players_order: List[Player]
    board: List[Estate]


class RunGameResponse(BaseModel):
    """Entidade response do processamento de um jogo completo."""

    winner: Player
    round_: int


class RunGamesResponse(BaseModel):
    """Entidade response do processamento de n jogos completos."""

    n_timeout: int
    mean_rounds: int
    victory_percentage: Dict[str, float]
    top_type: PlayerType
