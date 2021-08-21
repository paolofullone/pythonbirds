class Pessoa:
    def __init__(self, *filhos, nome=None, idade=20): # o *filhos permite que seja passada uma quantidade variada de
        # filhos na construção de uma pessoa.
        self.nome = nome # aqui temos um parametro nome e um atributo nome, o atributo é o que está conectado com o
        # self.nome, o parâmetro nome não utiliza self. Sempre que tiver o . é o nome do objeto self. Quando não temos
        # nada é respectivo a um parâmetro ou uma variável declarada no contexto do código.
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):  #poderia ser qq dois, em java o self é this, no python sempre colocamos self
        return f'Olá {id(self)}'

if __name__ == '__main__': # a main serve para fazermos os testes.
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
