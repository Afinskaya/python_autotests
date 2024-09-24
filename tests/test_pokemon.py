import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'trainer_token'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRANER_ID = 6409

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRANER_ID})
    assert response.status_code == 200

def test_name_trainer():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRANER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'isq'