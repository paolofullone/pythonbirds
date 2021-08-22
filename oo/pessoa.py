class Pessoa:
    olhos = 2 # este é um atributo default, se criarmos o olhos=2 dentro do __init__ junto com os demais atributos, o
    # python vai alocar um espaço em memória olhos=2 para cada pessoa criada no jogo, com o atributo default o python
    # cria apenas 1 espaço em memória para este atributo.
    def __init__(self, *filhos, nome=None, idade=20): # o *filhos permite que seja passada uma quantidade variada de
        # filhos na construção de uma pessoa.
        self.nome = nome # aqui temos um parametro nome e um atributo nome, o atributo é o que está conectado com o
        # self.nome, o parâmetro nome não utiliza self. Sempre que tiver o . é o nome do objeto self. Quando não temos
        # nada é respectivo a um parâmetro ou uma variável declarada no contexto do código.
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):  #poderia ser qq dois, em java o self é this, no python sempre colocamos self
        return f'Olá {id(self)}'

    @staticmethod # este é um decorator do python, tudo que começa com @ é um decorator.
    def metodo_estatico():
        return 40

    @classmethod
    def nome_e_atributos_de_classe(cls): # o pycharm já preenche o cls automaticamente
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__': # este if serve para fazermos os testes. os testes não serão impressos/exibidos quando o
    # arquivo pessoa.py for importado em outros módulos. Se executarmos o comando print(__name__) o resultado é __main__
    # ao executar o print(__name__) em outro módulo ele vai ter o nome da classe e não mais vai se chamar __main__

    paolo = Pessoa(nome='Paolo')
    luca = Pessoa(paolo, nome='Luca') # criamos o objeto luca que tem um filho paolo, este é um objeto complexo.
    print(Pessoa.cumprimentar(luca)) #agora vamos executar o método, Pessoa, pedimos o cumprimentar e passamos o pessoa.
    print(id(luca))
    print(luca.cumprimentar()) # Podemos executar o método a partir do objeto p e ter o mesmo resultado do
    # 'print(Pessoa.cumprimentar(p))'
    print(luca.nome) # é possível acessar o atributo através do próprio objeto com p.nome (atributo.nome)
    print(luca.idade)
    for filho in luca.filhos:
        print(filho.nome)

    luca.sobrenome='Fullone' # aqui estamos criando um atributo para um objeto em execução (dinamicamente), ou seja,
    # sem declarar no 'def__init__', o python permite que seja feito desta forma, porém este atributo se aplica somente
    # a este objeto 'luca', nenhum outro objeto desta classe será afetado. se pedirmos o paolo.sobrenome retornará um
    # erro.

    print(luca.sobrenome)
    # podemos usar o __dict__ para acessar todos os atributos de cada objeto:
    print(luca.__dict__) # aqui tem sobrenome
    print(paolo.__dict__) # aqui não tem.

    # Podemos remover os atributos dinamicamente também:
    del luca.filhos
    print()
    print(luca.__dict__) # agora o objeto luca não tem mais o atributo filhos, ainda que o atributo filhos tenha sido
    # criado no __init__.
    # Isso NÃO costuma ser uma boa prática. Mas pode ser útil, por exemplo pegar uma data e apresentar como formato
    # diferente somente em uma instância.

    print(f'Uma pessoa normal tem {Pessoa.olhos} olhos.') # Podemos acessar o atributo olhos diretamente da classe
    # Pessoa, pois ele é um atributo default. Porém se perguntarmos Pessoa.nome ou Pessoa.filhos vai retornar um erro
    # pois são atribudos de objetos da classe.

    print(f'A pessoa {luca.nome} tem {luca.olhos} olhos.')
    # observar que o __dict__ de Luca e Paolo não possuem o atributo de classe olhos. Caso seja alterado o número de
    # olhos de luca (luca.olhos = 1) o __dict__ de luca passa a ter o atributo olhos, porém o de Paolo não será
    # alterado. Caso desejemos alterar o atributo olhos para todas as pessoas devemos executar Pessoa.olhos = 3, assim o
    # impacto será em todas as pessoas criadas.

    print(Pessoa.metodo_estatico(), luca.metodo_estatico()) # com o decorator criado, da mesma forma podemos chamar o
    # método estático da classe ou do objeto.
    print(Pessoa.nome_e_atributos_de_classe(), luca.nome_e_atributos_de_classe()) # idem ao decorator static.