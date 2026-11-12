import requests
import json

def main():
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        agrupado_por_restaurante = {}
        for item in data:
            nome_do_restaurante = item['Company']
            if item['Company'] not in agrupado_por_restaurante:
                agrupado_por_restaurante[nome_do_restaurante] = []
            
            agrupado_por_restaurante[nome_do_restaurante].append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
            
        for restaurante, items in agrupado_por_restaurante.items():
            nome_arquivo = f'{restaurante}.json'
            with open(nome_arquivo, 'w') as f:
                json.dump(items, f, indent=4)

    else:
        print(f'status code: {response.status_code}')

if __name__ == '__main__':
    main()