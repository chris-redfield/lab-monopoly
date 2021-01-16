from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from routers import monopoly

from models.game import Game

app = FastAPI()

game_instance = Game()

app.include_router(
    monopoly.router,
    prefix='/monopoly',
	tags=['monopoly']
)