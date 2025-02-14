import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '08eacf5991cfaf750fe347337e00ec79'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '20285'

def test_status_code ():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
        response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
        assert response_get.json()["data"][0]["name"] == 'Шпингалет'

@pytest.mark.parametrize('key, value', [('name', 'Шпингалет'), ('trainer_id', TRAINER_ID), ('id', '234263')])
def test_parametrize(key, value):
      response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
      assert response_parametrize.json()["data"][0][key] == value

def test_status_code_trainers ():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response_name():
        response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
        assert response_get.json()["data"][0]["trainer_name"] == 'Cesaro'