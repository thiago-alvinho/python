from modelos.banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero

    def __str__(self):
        return f'nome: {self._nome} - endereço: {self._endereco} - numero: {self._numero}'