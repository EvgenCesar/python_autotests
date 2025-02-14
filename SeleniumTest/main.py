import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '08eacf5991cfaf750fe347337e00ec79'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "LOGIN",
    "password": "PASS"
    }
body_confirmation = {
    "trainer_token": TOKEN
    }
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
name_create = {

    "pokemon_id": "234263",
    "name": "Шпингалет",
    "photo_id": 22
}
add_pokeball = {
    "pokemon_id": "234263"
}
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)''' 

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)

message = response_create.json['message']
print(message)'''

'''response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = name_create)
print(response_create.status_code)'''

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = add_pokeball)
print(response_create.status_code)
