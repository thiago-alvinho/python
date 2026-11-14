import csv

# with open('dados.csv', 'w') as f:
#     escritor = csv.writer(f)
#     escritor.writerow(['Nome', 'Idade'])
#     escritor.writerow(['Thiago', 25])
#     f.close()

with open('dados.csv', newline='') as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)
    f.close()

# with open('dados.txt', 'a') as f:
#     f.write('last line')
#     f.close()
# 
# with open('dados.txt', 'r') as f:
#     dados = f.read()
#     print(dados)


#with open('dados.txt', 'w') as f:
#    f.write('Hello world')

# # ---------- Listas ------------
# lista = [1, 'python', ['something else']]
# print(lista)
# 
# # As listas são mutáveis
# lista[0] = 'IA vai roubar meu emprego?'
# print(lista)
# 
# # Adição de elementos
# lista.append('Someone')
# print(lista)
# lista.insert(2, 'In the middle')
# print(lista)
# 
# # ---------- Tuplas ------------
# t = 'some', 'thing', 'else'
# print(t)
# 
# # Tuplas são imutáveis
# # t[0] = 'other'
# 
# another_tuple = t, lista
# print(another_tuple)
# t2, lista2 = another_tuple
# print(t2)
# print(lista2)
# 
# # ---------- Dicionários ------------
# dicionario = {'someone': 0, 'middle': 1, 'else': 2}
# print(dicionario)
# print(dicionario['someone'])
# 
# dicionario['last'] = 3
# print(dicionario)
# 
# for k, i in dicionario.items():
#     print(k, i)