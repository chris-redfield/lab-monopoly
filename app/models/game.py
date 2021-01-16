from models.player import Player, PlayerType
from models.estate import Estate
import random
from operator import attrgetter


class Game:

    def init_game(self, seed):
        player_1 = Player(player_id=1,player_type=PlayerType.IMPULSIVE, balance=300)
        player_2 = Player(player_id=2,player_type=PlayerType.RIGOROUS, balance=300)
        player_3 = Player(player_id=3,player_type=PlayerType.CAUTIOUS, balance=300)
        player_4 = Player(player_id=4,player_type=PlayerType.RANDOM, balance=300)

        random.seed(seed)
        
        # atribui a ordem dos jogadores aleatoriamente
        players_list = [player_1, player_2, player_3, player_4]
        players_order = players_list.copy()
        random.shuffle(players_order)
        players_list.insert(0,None)
        
        ## Posição -1 é o ponto de partida
        ## após o começo do jogo essa posição deixa de existir
        ## ao passar novamente na posição 0, o jogador ganha 100
        board = []
        board.append(Estate(price=50, rent=10, estate_id = 0))
        board.append(Estate(price=100, rent=20, estate_id = 1))
        board.append(Estate(price=150, rent=30, estate_id = 2))
        board.append(Estate(price=200, rent=40, estate_id = 3))
        board.append(Estate(price=250, rent=55, estate_id = 4))
        board.append(Estate(price=300, rent=60, estate_id = 5))
        board.append(Estate(price=50, rent=10, estate_id = 6))
        board.append(Estate(price=100, rent=20, estate_id = 7))
        board.append(Estate(price=150, rent=30, estate_id = 8))
        board.append(Estate(price=200, rent=40, estate_id = 9))
        board.append(Estate(price=250, rent=55, estate_id = 10))
        board.append(Estate(price=300, rent=60, estate_id = 11))
        board.append(Estate(price=50, rent=10, estate_id = 12))
        board.append(Estate(price=100, rent=20, estate_id = 13))
        board.append(Estate(price=150, rent=30, estate_id = 14))
        board.append(Estate(price=200, rent=40, estate_id = 15))
        board.append(Estate(price=250, rent=55, estate_id = 16))
        board.append(Estate(price=300, rent=60, estate_id = 17))
        board.append(Estate(price=50, rent=10, estate_id = 18))
        board.append(Estate(price=100, rent=20, estate_id = 19))
        
        return players_list, players_order, board