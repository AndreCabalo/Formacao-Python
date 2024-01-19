import os
from modelos.avaliacao import Avaliacao

# Criando uma classe 
class Restaurante:
    '''Lista que ira armazenar os restaurantes'''
    restaurantes = []

    '''Método construtor'''
    def __init__(self,nome,categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        self._avaliacao = []

        '''Sempre que instanciar um restaurante, ja adiciona-lo a lista'''
        Restaurante.restaurantes.append(self)

    '''Método que imprime os dados do objeto'''
    def __str__(self):
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(25)} |{str(self.media_avaliacoes)} | {self.status.ljust(25)}'
    
    '''Método que lista todos os restaurantes da lista'''
    '''Usamos classmethod, quando não precisamos de uma instancia de objeto para acessar infos da classe'''
    @classmethod
    def listar_restaurantes(cls):
        os.system('cls')
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} |{'Avaliação'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(restaurante)

    @property
    def status(self):
        return 'Está aberto  ✅' if self._status else 'Está fechado ❌'

    def alterar_estado(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Ainda não tivemos avaliação'
        else:
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            quantidade_de_notas = len(self._avaliacao)
            media = round(soma_das_notas/quantidade_de_notas,1)
            return media
    

