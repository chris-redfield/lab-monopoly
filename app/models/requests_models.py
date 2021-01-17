from typing import List, Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel


class InitGameRequest(BaseModel):
    """Entidade request para inicialização de um jogo."""

    random_seed: int = 0


class ProcessRoundRequest(BaseModel):
    """Entidade request para processamento de uma rodada."""

    random_seed: int = 0


class RunGameRequest(BaseModel):
    """Entidade request para processamento de um jogo completo."""

    random_seed: int = 0


class RunGamesRequest(BaseModel):
    """Entidade request para processamento de n jogos completos."""

    random_seed: int = 0
    games_number: int = 10
