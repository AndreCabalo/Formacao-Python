from modelos.cardapio.item_cardapio import ItemCardapio

# Esta classe prato, irá herdará metodos e atributos da classe ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        #Usando o super classe, método init, passar nome e preco
        super().__init__(nome,preco)
        self.descricao = descricao

    def __str__(self):
        return f'{self._nome}'

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)