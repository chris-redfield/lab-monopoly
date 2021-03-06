from pydantic import BaseModel
from enum import Enum
from models.estate import Estate
import random

class PlayerType(str, Enum):
    """Tipo de Jogador"""

    IMPULSIVE = 'impulsive'
    RIGOROUS = 'rigorous'
    CAUTIOUS = 'cautious'
    RANDOM = 'random'

class Player(BaseModel):
    """Principal entidade do jogo. Move-se pelo tabuleiro, compra imóveis e coleta / paga aluguel"""

    player_id: int
    player_type : PlayerType = None
    balance:int
    estates:list = []
    position:int = -1

    def move(self):
        """Joga o dado e retorna a nova posição do jogador
        Caso supere a posição 19, continua do início.
        """

        dice_row = random.randint(1,6)

        print(f"player {self.player_id} rolled {dice_row}")

        new_position = self.position + dice_row

        #passou pela posição final, retorna ao início
        if(new_position > 19):
            self.position = (new_position % 10)
            # ganha 100 pela volta
            self.balance += 100

        #nao passou pela posição final
        else:
            self.position = new_position

        return self.position


    def buy(self, estate:Estate):
        """ Pergunta ao jogador se ele quer comprar a propriedade.
        Retorna se o jogador realizou a compra.
        """

        #nao pode comprar
        if(self.balance - estate.price < 0):
            return False
        #pode comprar
        else:
            # PlayerType.IMPULSIVE
            if(self.player_type == PlayerType.IMPULSIVE):  
                self.estates.append(estate)
                self.balance -= estate.price
                estate.owner = self.player_id
                return True
            
            # PlayerType.RIGOROUS
            elif(self.player_type == PlayerType.RIGOROUS):
                if(estate.rent>50):
                    self.estates.append(estate)
                    self.balance -= estate.price
                    estate.owner = self.player_id
                    return True
                else:
                    return False

            # PlayerType.CAUTIOUS
            elif(self.player_type == PlayerType.CAUTIOUS):
                if(self.balance - estate.price >= 80):
                    self.estates.append(estate)
                    self.balance -= estate.price
                    estate.owner = self.player_id
                    return True
                else:
                    return False
             
            # PlayerType.RANDOM
            elif(self.player_type == PlayerType.RANDOM):
                buy_intention = random.randint(0, 1)
                if(buy_intention == 1):
                    self.estates.append(estate)
                    self.balance -= estate.price
                    estate.owner = self.player_id
                    return True
                else:
                    return False


    def pay_rent(self, estate:Estate, estate_owner: 'Player'):
        """Realiza pagamento do aluguel e retorna se o jogador está falido.
        caso o jogador caia na própria propriedade, nada mudará.
        """
        self.balance -= estate.rent
        estate_owner.balance += estate.rent
        # Jogador tem saldo
        if(self.balance >= 0):
            return False
        # Jogador faliu
        else:
            # devolve as propriedades para o banco, retirando o registro de dono delas
            for estate_owned in self.estates:
                estate_owned.owner = None
            return True
