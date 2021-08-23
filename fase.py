# -*- coding: utf-8 -*-
from itertools import chain
from atores import ATIVO


VITORIA = 'VITORIA'
DERROTA = 'DERROTA'
EM_ANDAMENTO = 'EM_ANDAMENTO'


class Ponto():
    def __init__(self, x, y, caracter):
        self.caracter = caracter
        self.x = round(x)
        self.y = round(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.caracter == other.caracter

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __repr__(self, *args, **kwargs):
        return "Ponto(%s,%s,'%s')" % (self.x, self.y, self.caracter)


class Fase():
    def __init__(self, intervalo_de_colisao=1):
        """
        Método que inicializa uma fase.

        :param intervalo_de_colisao:
        """
        self.intervalo_de_colisao = intervalo_de_colisao
        self._passaros = []
        self._porcos = []
        self._obstaculos = []

        # Quando começamos um atributo com _ estamos dizendo que é um atributo protegido, que não deveria ser acessado
        # pelo usuário da biblioteca. Chamado de atributo protegido no Java por ex.

    def adicionar_obstaculo(self, *obstaculos):
        """
        Adiciona obstáculos em uma fase

        :param obstaculos:
        """
        self._obstaculos.extend(obstaculos)

    def adicionar_porco(self, *porcos):
        """
        Adiciona porcos em uma fase

        :param porcos:
        """
        self._porcos.extend((porcos))

    def adicionar_passaro(self, *passaros):
        """
        Adiciona pássaros em uma fase

        :param passaros:
        """
        self._passaros.extend((passaros))

    def status(self):
        """
        Método que indica com mensagem o status do jogo

        Se o jogo está em andamento (ainda tem porco ativo e pássaro ativo), retorna essa mensagem.

        Se o jogo acabou com derrota (ainda existe porco ativo), retorna essa mensagem

        Se o jogo acabou com vitória (não existe porco ativo), retorna essa mensagem

        :return:
        """
        if not self._possui_porco_ativo(): # quando usamos o _ antes do nome somente a própria classe ou uma de suas
            # subclasses pode fazer uso deste objeto. Trata-se de um objeto protegido. É interessante para que a
            # interface com o usuário externo seja bem limpa.
            return VITORIA
        elif self.possui_passaros_ativos(): #se possui porco e passaros está em andamento.
            return EM_ANDAMENTO
        else:
            return DERROTA # se não houver passaro ativo acabou em derrota.

    def lancar(self, angulo, tempo):
        """
        Método que executa lógica de lançamento.

        Deve escolher o primeiro pássaro não lançado da lista e chamar seu método lançar

        Se não houver esse tipo de pássaro, não deve fazer nada

        :param angulo: ângulo de lançamento
        :param tempo: Tempo de lançamento
        """
        for passaro in self._passaros:           # para cada pássaro na lista de passaros
            if not passaro.foi_lancado():        # verificar se o pássaro foi lançado, se ele não foi lançado
                passaro.lancar(angulo, tempo)    # lançar o pássaro com o ângulo e o tempo em que foi lançado.
                break                            # depois de encontrar o primeiro pássaro que vai ser lançado podemos parar o laço for.


    def calcular_pontos(self, tempo):
        """
        Lógica que retorna os pontos a serem exibidos na tela.

        Cada ator deve ser transformado em um Ponto.

        :param tempo: tempo para o qual devem ser calculados os pontos
        :return: objeto do tipo Ponto
        """
        pontos=[self._transformar_em_ponto(a) for a in self._passaros+self._obstaculos+self._porcos]

        return pontos

    def _transformar_em_ponto(self, ator):
        return Ponto(ator.x, ator.y, ator.caracter())

    def _possui_porco_ativo(self):
        for porco in self._porcos: # para cada porco na lista de porcos
            if porco.status = ATIVO;
            return True
        return False

    def possui_passaros_ativos(self):
        for passaro in self._passaros: # para cada passaro na lista de passaros
            if passaro.status = ATIVO;
            return True
        return False
    
        

