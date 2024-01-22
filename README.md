# Formacao-Python

Formação Python na Alura

Neste repositório você pode acessar meu próprio conteudo, no qual criei durante as aulas, além de ter acesso a todos exercicios que executei!

Intuito é deste repositório é documentar meu aprendizado e praticar git-github e JupyterNotebook.

  - Criarei um resumo neste arquivo readme.me, mas caso queira mais detalhes acesse os arquivos dentro da pasta "Conteudo", são arquivos no formato JupyterNotebook(.inpynb)

# Curso 1 - Python crie sua primeira aplicação

## Tipos de dados

|<b style="color:crimson"><b style="color:crimson">Tipo de dado| <b style="color:crimson">Nome técnico| <b style="color:crimson">Exemplo|
|------------|-------------|--------|
|Inteiro     | int         | 1      |
|Flutuante   | float       | 1.4    |
|Complexo    | complex     | 1w     |
|String      | str         | Hello Word |
|Boolean     | bool        | true/false    |
|List        | list        | ['Alexa','Jackeline','Beatriz','Patricia','Lohana'] |
|Tupla (imutáveis)      | tuple        | (1,2,3,4,5,6,7,8,9,10)|
|Dictinonary (chave:valor) | dic      | {'Lohana':10, 'Jackeline':8, 'Beatriz':9}|

## The Zen of Python

  - Poema que conseguimos atraves do comando no terminal Python:

      <code>import this</code>
      
## Manipulaçao de Strings</h1>

  - Diferença entre "aspas duplas" e 'aspas simples'
  
  - Uso de simbolos do site fsymbols
  
  - Interpolações com <code>f'Texto {variavel}'</code>
  
## Função Print()

   - Função print com f'' e sem 

## Função Input()

  - Função input com conversão de dados se preciso, com por exemplo:

    <code>numero = int(input('Digite um número))</code>

## Try Except

  - Onde temos um bloco try no qual tenta executar tais comando
    
  - Caso ocorra algum erro executa o except
    
  - <code>try:
         conta = 0/2
    except:
        Se não for possivel executar o try, tente este </code>

  ## Criando listas [   ]
  
 - Criando listas com suas funções como:
 
    * append, adicionar na lista
    
    * sum, soma os valores da lista
    
    * reverse, inverte a ordem da lista
    
    * len, conta quantas indices temos na lista
  
  ## Estruturas de repetições

  ### For

  - loop For com range e in
  - 
  - Onde queremos iterar sobre um bloco por determinado número de vezes

 ### While

   - Quando queremos interar sobre um bloco até que dada condição seja satisfeta

  ## Dict

  - Onde temos {chave:valor}

   ## Estruturas condicionais

### IF

- Onde verificamos uma códição e se verdadeira, executa o primeiro bloco

### ELIF

- Caso a condição não seja atendida, podemos testar esta, que caso seja atendada executa seu bloco

### ELSE

- Caso o bloco IF;ELIF não se atendido este será executado

  ## .ljust(x)

  - Para adicionar um espaçamento padrão a esquerda

# Curso 2 - Aplicando orientação a Objetos

## Classes e métodos

- Classe é a maneira no qual um objeto é classificado, podendo ser um objeto carro, um objeto pessoa entre outros.
- Uma classe é como uma forma de bolo, na qual possui atributos especificos, caso possua tais atributos, pode ser considerado de tal classe
- Por exemplo, um item classe carro, possui:
  * Rodas
  * Motor
  * Assentos
  * Placa
  * Chassi

## Métodos de classes
- Existem alguns métodos padrão das classes, entre eles:

  ### DIR, onde exibe os métodos de uma classe

    Exemplo de sintaxe:

    <code>print(dir(objeto))</code>

  ### VARS, onde exibe um dicionario com os atributos
  
    Exemplo de sintaxe:

    <code>print(vars(objeto))</code>
    
## Construtores

- Sempre que queremos criar uma instancia de um objeto, usaremos este método (ocultamente)

  Exemplo de sintaxe:

  <code>class Restaurante:
    def __init__(self, nome, categoria, status):        
          self.nome = nome 
          self.categoria = categoria
          self.status = status
        novo = Restaurante('Pizza Place', 'Fast Food', 'Ativo')</code>
    

## Dunder métodos

- Dunder methods ou métodos especiais, são aqueles com dois underlines __

  ### STR

  Usamos para caso tentamos imprimir diretamente um objeto, ele nos retorne algum texto pré definido

## Importando classes

- Para importar método devemos usar o comando <code> import nomeClasse </code>

## Property

- Usamos o Property, quando queremos modificar a maneira como um atributo é lido, principalmente em atributo com underline(privados)
- Para usar este property, devemos usar da seguinte maneira:

<code>@property
          def status(self):
              return f'Ativo' if self._status else 'Desativo'</code>

## Alguns métodos

### .Title()

- Usamos para fazer que a primeira letra das palavras, fiquem em maíuscuolo
  
### .Capitalize()
  
- Usamos para fazer que a primeira letra da primeira palavras, fique em maíuscuolo

### .Upper()
  
- Usamos para fazer que  todas letras se tornem maiúsculas

### .lower()
  
- Usamos para fazer que  todas letras se tornem minusculas
  
## Método de classe - @Classmethod

- Existe dois tipos conhecidos de métodos, os <t style="color:crimson">métodos de instancia</t>, onde usamos a instancia de um objeto da classe como parametro e também temos o <t style="color:springgreen">métodos de classe</t>, no qual usamos a classe como parametro, quando não precisamos utilizar nenhuma instancia para rodar este método, quando isso ocorrer, é fortemente recomendado que apontemos este metodo com <t style="color:springgreen">@classmethod</t>

Exemplo:

<code>class Carro:
    def __init__(self,modelo):
        self.modelo = modelo
    @classmethod
    def exibir_classe(self):
        return f'É um carro'    
print(f'Método de classe que mostra que: - {Carro.exibir_classe()}')</code>
