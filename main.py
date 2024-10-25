from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/v1/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da
    programação!
    '''
    return {'Hello' : 'world'}

@app.get('/api/v1/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code != 200:
        return f'Error:{response.status_code} - {response.text}'

    dados = response.json()
    if restaurante is None:
        return {'dados': dados}
    
    dados_restaurantes = []
    for item in dados:
        if item['Company'] == restaurante:
            dados_restaurantes.append({
                "item": item['Item'],
                "price": item['price'],
                "description": item['description']
            })
    
    return {'Restaurante': restaurante, 'Cardapio': dados_restaurantes}