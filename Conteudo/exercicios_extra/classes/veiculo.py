from abc import ABC, abstractclassmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractclassmethod
    def ligar(self):
        pass

    def __str__(self):
        return f'Sou um veículo : Marca {self.marca} | Modelo: {self.modelo}'