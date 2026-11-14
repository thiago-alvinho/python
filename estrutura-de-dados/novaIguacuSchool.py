import csv

with open('notas.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(['nome', 'nota'])
    w.writerow(['zezin', 5.0])
    w.writerow(['luizin', 8.0])
    w.writerow(['mariazinha', 10.0])
    w.writerow(['lulu', 6.0])
    f.close()

with open('notas.csv', newline='') as f:
    r = csv.reader(f)
    for linha in r:
        nome, nota = linha
        if nota == 'nota': continue
        nota = float(nota)
        if nota >= 7:
            print(f'Parabéns {nome}, você passou direto com nota {nota}!')

