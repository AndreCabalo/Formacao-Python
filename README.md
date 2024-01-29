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


# Curso 3 - Avance na Orientação a Objetos e consuma API

## Herança

Usamos o conceito de herança para otimizar e reaproveitar um código ja existente, ganhando assim, tempo de execução e compreensão.

* Por exemplo, temos um item do cardapio, sendo que todo item do cardapio possui (nome, preço),

* Temos também os pratos e bebidas, que também possui algunas caracteristicas iguais a item do cardapio, como (nome,preço) e mais algumas exclusivas.

* Por tanto para usaremos herança devemos fazer o seguinte:

    - Importar a classe que queremos herdar, dentro da classe filha

    - Adicionar o nome da classe mãe dentro de um parenteses na frente do nome da classe
    
    - Chamar o super( ) e acessar o construtor da mãe

* Observações:

    - A classe filha, herda os atributos e métodos da classe mãe, e se quiser sobrepor estas, pode, mas veremos em breve isso em polimorfismo

## Classe abstrata

Classe abstrata é aquela que não instancia algo e obriga seus filhos a criarem o mesmo método com mesmo nome, obrigatório:

* Importar ABC e abstractclassmethod

* Lembrar que não queremos que a classe crie/instancia

* Adicionar o decorator @abstractmethod a cima do método

* Lembrar que a classe que tem este método abstract deve herdar de ABC, por tanto colocar o (ABC), apos o nome da classe

* Todos os filhos desta classe, teram este método abstract obrigatóriamente, isso mesmo devemos criar o método abstract em todos os filhos/as

## Polimorfismo

Polimorfismo é quando um método da classe mãe, se comporta diferente nas classes filhas, inclusive podendo ser diferente em cada classe filha

* Mas um coisa boa! Podemos implantar o mesmo método, porém com diferença em cada uma das classes filhas, isso se chama polimorfismo

* Por exemplo, classe prato e classe bebida, herdam de itemCardapio, mas bebida tem 10% de desconto e prato tem 5% de desconto

## Ambientes virtuais

Resumidamente, é como se tivessemos um microcomputador dentro do nosso computador.

Para que nosso sistema possa rodar de forma similar para todos os devs envolvidos, o ideal é que criemos um ambientes virtual com as mesma condições, como por exemplo:

* Com mesma versão do Python
* Mesma versão do Flask

<i>Isso evita que o sistema quebre e aquele famoso jargão "Ahh mas no meu PC roda"</i>


Por tanto, nosso primeiro passo é :

* Aprender a preparar este ambiente virtual

* Aprender a puxar o ambiente virtual de outra pessoa
Para criar esta VENV, devemos:

1 - No VsCode em uma pasta nova, no terminal, usamos o comando:

    <code>python -m venv nome-que-queremos-para-venv</code>

Onde:

| Comando                     | Descrição                              |
|-----------------------------|----------------------------------------|
|python                       |  Para indicar um comando python        |
|-m                           |  Para indicar a criação de um modulo   |
|venv                         |  Para indicar a criação de uma venv    |
|nome-que-queremos-para-venv  |  É o nome escolhido para a nossa venv  |

Ao fazer isso, o python cria automaticamente um ambiente virtual

* A boa prática, recomenda usarmos o nome da venv de venv ou env, especificamente

Ativando o ambiente virtual:

no Windows:

<code>venv\Scripts\activate.bat</code>

## Requisições JSON e arquivos

 Requisição

Inserindo conteudo de restaurantes via JSON

Abrimos o ambiente virtual como ja haviamos feito com <code>venv\Scripts\activate.bat</code>

Em seguida criamos um arquivo "app.py"

e nele adicionamos o seguinte:

<code>
import requests


url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'


response = requests.get(url)


print(response)</code>

... este conteúdo pode ser melhor explorado dentro do arquivo na pasta Conteúdo deste repositório

## FastAPI

É um framework que facilita a criação de end-points que podem guardar métodos e conteúdo.

Antes de utiliza-lo devemos instalar o FastAPI no pc ou ambiente virtual, da seguinte maneira:

<code>pip install fastapi</code>

e em seguida:

<code>pip install uvicorn</code>

Apos isso, vamos criar um arquivo "main.py" apenas para diferenciar do "app.py"

e iremos inserir nele:

<code>from fastapi import FastAPI
app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'Hello':'World'}</code>

Apos inserir os dados a cima no arquivo "main" devemos estar dentro do diretório do arquivo main (no terminal, se preciso navegue até la com o comando <code>CD nomePasta</code>)

Em seguida digite no terminal :<code>uvicorn main:app --reload </code>

Após isso o terminal mostrará inumeras informações, inclusive o end-point (o endereço local-host )

Ao entrar no link, vc verá que surgiu um erro e que nada foi encontrado, para sanar isto, basta adicionaro end-point criado no final do endereço, por exemplo:

<code>/api/hello</code>

Exatamente como indicamos no arquivo "main.py"



