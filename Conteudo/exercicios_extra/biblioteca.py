import os
from livros import Livro

class Biblioteca:
    def __init__(self, nome_biblioteca):
        self.nome_biblioteca = nome_biblioteca


game_of_thrones = Livro('As Crônicas de Gelo e Foco', 'George R.R Martin','1996')
print(game_of_thrones)

#Emprestando livro
game_of_thrones.emprestar()
print(game_of_thrones)

Livro.verificar_disponibilidade('1996')
