from modelos.avaliacao import Avaliacao
from modelos.cardapio.itemCardapio import ItemCardapio

class Restaurante:
    """Classe restaurante e suas propriedades"""
    restaurantes = []
    
    def __init__(self, nome = '', categoria = ''):
        """
        Método de inicialização de uma instância restaurante.
        
        Parâmetros:
        - nome(str): Nome do restaurante
        - categoria(str): Categoria do restaurante

        """
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self.ativo} | {'Sem avaliação' if self.media_avaliacoes == -1 else self.media_avaliacoes}'

    @property
    def ativo(self):
        return '✓' if self._ativo else '✗'

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return -1 
        else: 
            soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
            quantidade_notas = len(self._avaliacoes)
            return round(soma_notas / quantidade_notas, 1)

    @property
    def cardapio(self):
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_tipo'):
                print(f'{i}. {item._nome} | Preço: {item._preco} | Tipo: {item._tipo} | Tamanho: {item._tamanho} | Descricao: {item._descricao}')
            elif hasattr(item, '_tamanho'):
                print(f'{i}. {item._nome} | Preço: {item._preco} | Tamanho: {item._tamanho}')
            else:
                print(f'{i}. {item._nome} | Preço: {item._preco} | Descricao: {item._descricao}')

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(restaurante)

    def avaliar_restaurante(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    def adicionar_item_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
            


# class Pessoa:
#     def __init__(self, nome = '', idade = int, profissao = ''):
#         self._nome = nome
#         self._idade = idade
#         self._profissao = profissao
#     
#     def __str__(self):
#         return f'{self._nome} tem {self._idade} anos e atua na profissao {self._profissao}'
#     
#     def aniversario(self):
#         self._idade = self._idade + 1
#     
#     @property
#     def saudacao(self):
#         print(f'Bem-vindo, a profissao {self._profissao} eh muito valorizada por aqui!')
# 
# pessoa1 = Pessoa('Thiago', 25, 'Desenvolvedor')
# print(pessoa1)
# pessoa1.saudacao
# 
# class Musica:
#     musicas = []
# 
#     def __init__(self, nome = '', artista = '', duracao = 0):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao
#         Musica.musicas.append(self)
# 
#     def __str__(self):
#         return f'{self.nome} - {self.artista} - {self.duracao}'
#     
#     def listar_musicas():
#         for musica in Musica.musicas:
#             print(f'{musica.nome} - {musica.artista} - {musica.duracao}')
# 
# musica1 = Musica('i dont know', 'someone', 1000)
# musica2 = Musica('something cool', 'someone great', 2000)

# Musica.listar_musicas()

# Criação de classes sem método init
# class Restaurantes:
#     nome = ''
#     categoria = ''
#     ativo = False
# 
# restaurante1 = restaurantes()
# restaurante2 = restaurantes()
# 
# restaurantes = [restaurante1, restaurante2]
# 
# restaurante1.nome = 'Delicias da lulu'
# restaurante1.categoria = 'Salgadinhos e doces'
# print(vars(restaurantes[0]))
# 
# class Musica:
#     nome = ''
#     artista = ''
#     duracao = 0
# 
# musica1 = musica()
# musica2 = musica()
# musica3 = musica()
# 
# musica1.nome = 'i dont know'
# musica1.artista = 'someone'
# musica1.duracao = 10000
# 
# print(vars(musica1))