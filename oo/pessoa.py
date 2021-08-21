class Pessoa:
    def cumprimentar(self):  #poderia ser qq dois, em java o self é this, no python sempre colocamos self
        return f'Olá {id(self)}'

if __name__ == '__main__': # a main serve para fazermos os testes.
    p = Pessoa() # criamos uma pessoa p
    print(Pessoa.cumprimentar(p)) #agora vamos executar o método, Pessoa, pedimos o cumprimentar e passamos o pessoa.
    print(id(p))
    print(p.cumprimentar()) # Podemos executar o método a partir do objeto p e ter o mesmo resultado do 'print(Pessoa.cumprimentar(p))'
