from models.player import Player, PlayerType
from models.estate import Estate
import random
from operator import attrgetter


class Game:

    players_list = None
    players_order = None
    board = None
    round_ = None

    ## Inicializa um novo jogo
    def init_game(self, seed):
        player_1 = Player(player_id=1,player_type=PlayerType.IMPULSIVE, balance=300)
        player_2 = Player(player_id=2,player_type=PlayerType.RIGOROUS, balance=300)
        player_3 = Player(player_id=3,player_type=PlayerType.CAUTIOUS, balance=300)
        player_4 = Player(player_id=4,player_type=PlayerType.RANDOM, balance=300)

        # retira random seed por hora
        #random.seed(seed)
        
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
        
        self.players_list = players_list
        self.players_order = players_order
        self.board = board
        self.round_ = 0

        return players_list, players_order, board

    # Executa uma rodada, elimina jogadores com menos de 0 de saldo
    # retorna o estado atual do jogo
    def process_single_round(self, seed):
        
        ## Caso não haja game inicializado, inicia um novo
        if(self.players_list == None):
            self.init_game(seed)

        self.round_ += 1

        players_list = self.players_list
        players_order = self.players_order
        board = self.board

        for player in players_order:
            print(f"player {player.player_id} in position", player.position)
            
            player_current_pos = player.move()
            print("new player position:", player_current_pos)
            
            current_estate = board[player_current_pos]
                
            estate_owner = current_estate.owner

            if estate_owner == None:
                player.buy(current_estate)
            
            else:

                estate_owner = players_list[estate_owner]
                
                print(f"player {player.player_id} is on player {estate_owner.player_id} property!")
                bankrupt = player.pay_rent(current_estate, estate_owner)

                #falido, remove o jogador do jogo
                if bankrupt:
                    print(f"player {player.player_id} went bankrupt")
                    players_order.remove(player)
        
        

        return players_list, players_order, board

    # Executa uma rodada, elimina jogadores com menos de 0 de saldo
    # Retorna caso haja um vencedor
    # Metodo criado para ser usado em conjunto com o run_game
    def process_round(self, players_list, players_order, board):
        self.round_ += 1
        
        for player in players_order:
            print(f"player {player.player_id} in position", player.position)
            
            player_current_pos = player.move()
            print("new player position:", player_current_pos)
            
            current_estate = board[player_current_pos]
                
            estate_owner = current_estate.owner

            if(estate_owner == None):
                player.buy(current_estate)
            
            else:

                estate_owner = players_list[estate_owner]
                
                print(f"player {player.player_id} fell on player {estate_owner.player_id} property!")
                bankrupt = player.pay_rent(current_estate, estate_owner)

                #falido, remove o jogador do jogo
                if(bankrupt):
                    print(f"player {player.player_id} went bankrupt")
                    players_order.remove(player)
                    
                    if(len(players_order) > 1):
                        return False
                    else:
                        return True

    ## Executa uma iteração completa de um game, ou finaliza o game atual
    def run_game(self, seed):
        
        ## Caso não haja game inicializado, ou haja um game finalizado, inicia um novo
        if self.players_list == None or len(self.players_order) == 1:
            players_list, players_order, board = self.init_game(seed)
        else:
            players_list = self.players_list
            players_order = self.players_order
            board = self.board
        
        while self.round_ < 1000:
            print(f"round {self.round_ + 1}")
            winner = self.process_round(players_list, players_order, board)
            if winner:
    #             print("the winner is:", players_order[0])
                return players_order[0], self.round_ + 1
            else:
                continue
                
        # caso o jogo ainda não tenha acabado
        winner = max(players_order, key=attrgetter('balance'))
        self.players_order = [winner]
        print("the winner is", winner)
        
        return winner, self.round_ + 1