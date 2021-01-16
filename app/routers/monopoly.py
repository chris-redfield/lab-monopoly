from typing import List, Optional
from fastapi import APIRouter
from fastapi import Query

import logging

from models.response_models import InitGameReturn

from models.requests_models import InitGameRequest

import main

router = APIRouter()

logger = logging.getLogger("api")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("QED.log")
fh.setLevel(logging.ERROR)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


@router.post('/new_game', response_model=InitGameReturn)
async def fixation_sequence(init_game_request: InitGameRequest):
	"""Processa e retorna a imagem original com identificação da sequência de fixação."""

	random_seed = init_game_request.random_seed

	players_list, players_order, board = main.game_instance.init_game(random_seed)

	# logger.info(players_list)
	# logger.info(players_order)
	# logger.info(board)
	players_list_return = players_list.copy()
	players_list_return.pop(0)

	return InitGameReturn(players_list=players_list_return, players_order=players_order, board=board)
