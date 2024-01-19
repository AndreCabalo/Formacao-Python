import os
# Criando uma classe 
class Restaurante:
    '''Lista que ira armazenar os restaurantes'''
    restaurantes = []

    '''Método construtor'''
    def __init__(self,nome,categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False

        '''Sempre que instanciar um restaurante, ja adiciona-lo a lista'''
        Restaurante.restaurantes.append(self)

    '''Método que imprime os dados do objeto'''
    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(25)} | {self.status.ljust(25)}'
    
    '''Método que lista todos os restaurantes da lista'''
    '''Usamos classmethod, quando não precisamos de uma instancia de objeto para acessar infos da classe'''
    @classmethod
    def listar_restaurantes(cls):
        os.system('cls')
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(restaurante)

    @property
    def status(self):
        return 'Está aberto  ✅' if self._status else 'Está fechado ❌'
    

    def alterar_estado(self):
        self._status = not self._status
    
# Instanciando algumas classes (criando alguns objetos) 
restaurante_praca = Restaurante('praça','Italiano')
restaurante_praca.alterar_estado()
restaurante_rococo = Restaurante('rcoco','Italiano')
restaurante_mandu = Restaurante('mandu','Arâbe')
restaurante_coco_bambu = Restaurante('coco Bambu','Italiano')
restaurante_outback = Restaurante('outback','Australiano')

#Printar todos os restaurantes da lista
Restaurante.listar_restaurantes()


