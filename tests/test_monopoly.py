from fastapi.testclient import TestClient
from app.main import app
import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath)

client = TestClient(app)

def test_new_game():
    """Testa se um novo game é criado corretamente"""
    request_dict = {'seed': 0}
    response = client.post("/monopoly/new_game", json=request_dict)
    assert response.status_code == 200
    print(response.json())
    print(type(response.json()))
    assert response.json()['players_list'] == [{'player_id': 1, 'player_type': 'impulsive', 
        'balance': 300, 'estates': [], 'position': -1}, {'player_id': 2, 'player_type': 'rigorous', 
        'balance': 300, 'estates': [], 'position': -1}, {'player_id': 3, 'player_type': 'cautious', 
        'balance': 300, 'estates': [], 'position': -1}, {'player_id': 4, 'player_type': 'random', 
        'balance': 300, 'estates': [], 'position': -1}]


def test_process_round():
    """Testa o processamento de uma rodada, checa se os jogadores realmente andaram no tabuleiro"""

    request_dict = {'seed': 0}
    response = client.post("/monopoly/process_round", json=request_dict)
    assert response.status_code == 200
    assert response.json()['players_list'][0]['position'] != -1


def test_run_game():
    """Testa um jogo completo, verifica se há algo errado com a rodada e se o vencedor tem saldo"""

    request_dict = {'seed': 0}
    response = client.post("/monopoly/run_game", json=request_dict)
    assert response.status_code == 200
    assert response.json()['round_'] > 1
    assert response.json()['winner']['balance'] > 0
