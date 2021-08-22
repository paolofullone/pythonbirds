


"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes.

Motor
Direção

O motor terá a responsabilidade de controlar a velocidade. Ele oferece os seguintes atributos:
1 - Atributo de dado Velocidade.
2 - Método acelerar que deverá incrementar a velocidade de uma unidade.
3 - Método frear que deverá decrementar a velocidade em duas unidades.

A direção terá a responsabilidade de controlar a direção. Ela ofecere os seguintes atributos:
1 - Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste
2 - Método girar_a_direita (se está em N e gira a direita vai para L, se gira a direita de novo vai para O...)
3 - Método girar_a_esquerda (se está em N e gira a esquerda vai para O, se gira a esquerda de novo vai para S...)
    N
O       L
    S

        Exemplo:
        # Testando motor.
        >>> motor = Motor() # ao clicar com o botão direito no pycharm e executar "run doctests" vão retornar vários erros.
        >>> motor.velocidade
        0
        >>> motor.acelerar()
        >>> motor.velocidade
        1
        >>> motor.acelerar()
        >>> motor.velocidade
        2
        >>> motor.acelerar()
        >>> motor.velocidade
        3
        >>> motor.frear()
        >>> motor.velocidade
        1
        >>> motor.frear()
        >>> motor.velocidade
        0

        # Testando direção
        >>> direcao = Direcao()
        >>> direcao.valor
        'Norte'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Leste'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Sul'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Oeste'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Norte'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Oeste'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Sul'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Leste'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Norte'
        >>> carro = Carro(direcao, motor)
        >>> carro.calcular_velocidade()
        0
        >>> carro.acelerar()
        >>> carro.calcular_velocidade()
        1
        >>> carro.acelerar()
        >>> carro.calcular_velocidade()
        2
        >>> carro.frear()
        >>> carro.calcular_velocidade()
        0
        >>> carro.calcular_direcao()
        'Norte'
        >>> carro.girar_a_direita()
        >>> carro.calcular_direcao()
        'Leste'
        >>> carro.girar_a_esquerda()
        >>> carro.calcular_direcao()
        'Norte'
        >>> carro.girar_a_esquerda()
        >>> carro.calcular_direcao()
        'Oeste'

"""
# Primeiro criamos a classe direção e todos seus cálculos e movimentos;
# Segundo criamos a classe Motor;
# Por último criamos a classe carro, chamando os cálculos do motor e da direção.

class Carro():
    def __init__(self, direcao, motor): #alt + enter em cima de direção cria o self.direcao = direcao automaticamente.
        self.motor = motor
        self.direcao = direcao

    # Na classe motor já definimos como o carro acelera, freia e qual sua velocidade, portanto na classe carro só
    # precisamos retornar estes cálculos nos respectivos métodos.
    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

NORTE='Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'

class Direcao():
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
    # Poderia resolver com vários if else, mas nessa estrutura o dicionário funciona melhor e o código fica mais limpo.


    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Motor():
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade=max(0, self.velocidade) # entre o valor 0 e o valor da velocidade atual, prevalece o maior,
        # usamos esta função para o carro não ter velocidade negativa, sempre que for maior que zero permanece a
        # velocidade atual do carro.


# Uma convenção da PEP8 diz que se uma variável não deve ter seu valor alterado (constante) seu nome deve ser em caixa
# alta. O Python não vai impedir que seu valor seja alterado, por isso é uma convenção.
