from modelos.restaurantes import Restaurante
# from modelos.agencia import Agencia
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa
def main():
    restaurante1 = Restaurante('Delicias da lulu', 'Salgadinhos e doces')
    print(restaurante1)
    prato1 = Prato('salgadinho', 2.00, 'Salgadinho da lulu')
    bebida1 = Bebida('suco de abacaxi', 3.00, 'Grande')
    sobremesa1 = Sobremesa('Bolo de cenoura', 5.00, 'Bolo', 'Medio', 'Bolo da lulu')
    restaurante1.adicionar_item_no_cardapio(prato1)
    restaurante1.adicionar_item_no_cardapio(bebida1)
    restaurante1.adicionar_item_no_cardapio(sobremesa1)
    restaurante1.cardapio

if __name__ == '__main__':
    main()