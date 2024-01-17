# Criando uma classe 
class Restaurante:
    '''Lista que ira armazenar os restaurantes'''
    restaurantes = []

    '''Método construtor'''
    def __init__(self,nome,categoria,ativo):
        self.nome = nome
        self.categoria = categoria
        self.status = False

        '''Sempre que instanciar um restaurante, ja adiciona-lo a lista'''
        Restaurante.restaurantes.append(self)

    '''Método que imprime os dados do objeto'''
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.status}'
    
    '''Método que lista todos os restaurantes da lista'''
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

# Instanciando algumas classes (criando alguns objetos) 
restaurante_praca = Restaurante('Praça','Italiano',True)
restaurante_rococo = Restaurante('Rococo','Italiano',True)
restaurante_mandu = Restaurante('Mandu','Arâbe',True)
restaurante_coco_bambu = Restaurante('Coco Bambu','Italiano',True)
restaurante_outback = Restaurante('Outback','Australiano',True)

#Printar todos os restaurantes da lista
Restaurante.listar_restaurantes()

