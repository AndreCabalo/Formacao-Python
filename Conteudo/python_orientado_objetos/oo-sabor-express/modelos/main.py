from livros import Livro
import os

star_wars = Livro('Star Wars - Invasão Rebelde', 'Zacks Nider','2024')
star_wars2 = Livro('Star Wars - Moon Rebel', 'Zacks Nider','2023')

Livro.verificar_disponibilidade('2021')


print(star_wars)
print(star_wars2)