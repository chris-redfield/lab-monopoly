from typing import List, Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel

class InitGameRequest(BaseModel):
	random_seed: int = 0

class ProcessRoundRequest(BaseModel):
	random_seed: int = 0

class RunGameRequest(BaseModel):
	random_seed: int = 0

class RunGamesRequest(BaseModel):
	random_seed: int = 0
	games_number: int = 10