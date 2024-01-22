from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self,marca, modelo, cor):
        super().__init__(marca,modelo)
        self.cor = cor

    def ligar(self):
        print('vrummm carro')

    def __str__(self):
        return f'Sou um veículo, mas especificamente um Carro, Marca:{self.marca} | Modelo: {self.modelo}'