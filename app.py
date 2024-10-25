import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code != 200:
    print(f'Error:{response.status_code}')

dados = response.json()
dados_restaurantes = {}
for item in dados:
    nome_do_restaurante = item['Company']
    if nome_do_restaurante not in dados_restaurantes:
        dados_restaurantes[nome_do_restaurante] = []
    dados_restaurantes[nome_do_restaurante].append({
        "item": item['Item'],
        "price": item['price'],
        "description": item['description']
    })

for nome_do_restaurante, dados in dados_restaurantes.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as file:
        json.dump(dados, file, indent=4)