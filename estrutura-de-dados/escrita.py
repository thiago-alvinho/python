nome = input('Escreva seu nome:')
idade = input('Escreva sua idade:')

with open('dados.txt', 'w') as f:
    f.write(f'Nome: {nome}\n')
    f.write(f'Idade: {idade}\n')
    f.close()