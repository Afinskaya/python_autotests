import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'trainer_token'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
body_born = {
    "name": "generate",
    "photo_id": -1
}
body_name = {
    "pokemon_id": "74480",
    "name": "Hmurik"
}
body_pokeball = {
    "pokemon_id": "74480"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_born)
print(response.text)'''

'''response_new_name = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_new_name.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)