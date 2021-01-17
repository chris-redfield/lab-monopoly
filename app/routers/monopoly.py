from typing import List, Optional
from fastapi import APIRouter
from fastapi import Query

import logging

from models.response_models import GameStateResponse, RunGameResponse, RunGamesResponse

from models.requests_models import InitGameRequest, ProcessRoundRequest, RunGameRequest, RunGamesRequest

import main

router = APIRouter()

logger = logging.getLogger("api")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("QED.log")
fh.setLevel(logging.ERROR)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


@router.post('/new_game', response_model=GameStateResponse)
async def new_game(init_game_request: InitGameRequest):
    """Inicializa um novo jogo, reinicia todos os valores"""

    random_seed = init_game_request.random_seed

    players_list, players_order, board = main.game_instance.init_game(
        random_seed)

    # logger.info(players_list)
    # logger.info(players_order)
    # logger.info(board)
    players_list_return = players_list.copy()
    players_list_return.pop(0)

    return GameStateResponse(players_list=players_list_return, players_order=players_order, board=board)


@router.post('/process_round', response_model=GameStateResponse)
async def process_round(process_round_request: ProcessRoundRequest):
    """Processa uma rodada e retorna o estado atual do jogo"""

    random_seed = process_round_request.random_seed

    players_list, players_order, board = main.game_instance.process_single_round(
        random_seed)
    players_list_return = players_list.copy()
    players_list_return.pop(0)

    return GameStateResponse(players_list=players_list_return, players_order=players_order, board=board)


@router.post('/run_game', response_model=RunGameResponse)
async def run_game(run_game_request: RunGameRequest):
    """Executa um jogo inteiro, retorna o vencedor e o número de partidas."""

    random_seed = run_game_request.random_seed

    winner, round_ = main.game_instance.run_game(random_seed)

    return RunGameResponse(winner=winner, round_=round_)


@router.post('/run_games', response_model=RunGamesResponse)
async def run_games(run_games_request: RunGamesRequest):
    """Executa n jogos, retorna o número time outs, a média de turnos por partida, 
    a percentagem de vitória por tipo de jogador e o tipo de jogador que mais ganha."""

    random_seed = run_games_request.random_seed
    games_number = run_games_request.games_number

    n_timeout, mean_rounds, victory_percentage, top_type = main.game_instance.run_games(
        random_seed, games_number)

    return RunGamesResponse(n_timeout=n_timeout, mean_rounds=mean_rounds, 
		victory_percentage=victory_percentage, top_type=top_type)
