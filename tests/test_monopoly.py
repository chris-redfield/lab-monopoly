from fastapi.testclient import TestClient
from app.main import app
import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath)

client = TestClient(app)


def test_new_game():
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

