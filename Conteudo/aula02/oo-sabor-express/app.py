# Da pasta modelos>restaurante, importe a classe Restaurant
from modelos.restaurante import Restaurante


def main():
    # Instanciando algumas classes (criando alguns objetos) 
    restaurante_praca = Restaurante('praça','Italiano')
    restaurante_praca.alterar_estado()
    restaurante_praca.receber_avaliacao('Fulano', 9)
    restaurante_praca.receber_avaliacao('Cigrano',9)
    restaurante_praca.receber_avaliacao('Lohana', 9)

    Restaurante.listar_restaurantes()
    

# Se for o arquivo principal, execute o main()
if __name__ == '__main__':
    main()