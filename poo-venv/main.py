from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/')
def hello_world():
    return {'hello': 'world'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para acessar o cardápio dos restaurantes

    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if restaurante == None:
             return {'Dados': data}

        dados_restaurante = []
        for item in data:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                        'item': item['Item'],
                        'price': item['price'],
                        'description': item['description']
                    })
        return {restaurante: dados_restaurante}
    
    else:
        return {'Erro': 'Falha na requisição dos dados'}