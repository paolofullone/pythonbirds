class Pessoa:
    def __init__(self, nome=None, idade=20):
        self.nome = nome # aqui temos um parametro nome e um atributo nome, o atributo é o que está conectado com o
        # self.nome, o parâmetro nome não utiliza self. Sempre que tiver o . é o nome do objeto self. Quando não temos
        # nada é respectivo a um parâmetro ou uma variável declarada no contexto do código.
        self.idade = idade

    def cumprimentar(self):  #poderia ser qq dois, em java o self é this, no python sempre colocamos self
        return f'Olá {id(self)}'

if __name__ == '__main__': # a main serve para fazermos os testes.
    p = Pessoa('Luca') # criamos uma pessoa p e atribuimos o nome 'Luca'
    print(Pessoa.cumprimentar(p)) #agora vamos executar o método, Pessoa, pedimos o cumprimentar e passamos o pessoa.
    print(id(p))
    print(p.cumprimentar()) # Podemos executar o método a partir do objeto p e ter o mesmo resultado do
    # 'print(Pessoa.cumprimentar(p))'
    print(p.nome) # é possível acessar o atributo através do próprio objeto com p.nome (atributo.nome)
    p.nome = 'Paolo' # é possível alterar o atributo de um objeto
    print(p.nome) # agora o objeto tem o valor 'Paolo'
    print(p.idade)
