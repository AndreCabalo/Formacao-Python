class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True 

        '''Adicionando livro a lista de livros'''
        Livro.livros.append(self)


    def __str__(self):
        return f'{self.titulo.ljust(35)} | {self.autor.ljust(25)} | {self.ano_publicacao.ljust(25)} | {self.disponivel}'
    
    def emprestar(self):
        self.disponivel = False

    def verificar_disponibilidade(ano_buscado):
        encontrado = False

        for livro in Livro.livros:
            if livro.ano_publicacao == ano_buscado:
                if livro.disponivel:
                    encontrado = True
                    print(f'Encontrei o livro : {livro}')

        if not encontrado:
            print(f'Nenhum livro encontrado no ano de : {ano_buscado}')
                
              

    


# print(game_of_thrones)
# game_of_thrones.emprestar()
# print(game_of_thrones)
# print(spider_verse)
# print(arte_da_guerra)

# Livro.verificar_disponibilidade('2019')
