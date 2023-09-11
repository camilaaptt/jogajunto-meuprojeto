import requests

squad = {
    "Camila": "66080472",
    "Clislânia": "60336070",
    "João Paulo": "41204355",
    "Lucas": "40353030"
}

for nome, cep in squad.items():
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    cidade = data['localidade']
    print(f'{nome}: {cidade}')

