# Da pasta modelos>restaurante, importe a classe Restaurant
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa


restaurante_praca = Restaurante('Praça','Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2.0 , 'O melhor pão da Cidade')
prato_paozinho.aplicar_desconto()
sobremesa_sorvete = Sobremesa('Sorvete', 15.0, 'Sorvete de creme belga','Gelado','200ml')
sobremesa_sorvete.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_sorvete)


def main():

    restaurante_praca.exibir_cardapio


# Se for o arquivo principal, execute o main()
if __name__ == '__main__':
    main()