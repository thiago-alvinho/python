class Banco:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    def __str__(self):
        return f'nome: {self._nome} - endereço: {self._endereco}'