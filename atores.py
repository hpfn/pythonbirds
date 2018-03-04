# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import math

DESTRUIDO = 'Destruido'
ATIVO = 'Ativo'
GRAVIDADE = 10  # m/s^2


class Ator():
    """
    Classe que representa um ator. Ele representa um ponto cartesiano na tela.
    """
    _caracter_ativo = 'A'
    _caracter_destruido = ' '

    def __init__(self, x=0, y=0):
        """
        Método de inicialização da classe. Deve inicializar os parâmetros x, y, caracter e status

        :param x: Posição horizontal inicial do ator
        :param y: Posição vertical inicial do ator
        """
        self.y = y
        self.x = x
        self.status = ATIVO

    def caracter(self):
        return self._caracter_ativo if self.status == ATIVO else self._caracter_destruido

    def calcular_posicao(self, tempo):
        """
        Método que calcula a posição do ator em determinado tempo.
        Deve-se imaginar que o tempo começa em 0 e avança de 0,01 segundos

        :param tempo: o tempo do jogo
        :return: posição x, y do ator
        """
        if tempo == 0:
            return 0, 0
        return self.x * (tempo/10), self.y * (tempo/10)

    def colidir(self, outro_ator, intervalo=1):
        """
        Método que executa lógica de colisão entre dois atores.
        Só deve haver colisão se os dois atores tiverem seus status ativos.
        Para colisão, é considerado um quadrado, com lado igual ao parâmetro intervalo, em volta do ponto onde se
        encontra o ator. Se os atores estiverem dentro desse mesmo quadrado, seus status devem ser alterados para
        destruido, seus caracteres para destruido também.

        :param outro_ator: Ator a ser considerado na colisão
        :param intervalo: Intervalo a ser considerado
        :return:
        """
        if self.status == ATIVO and outro_ator.status == ATIVO:
            if self.x == outro_ator.x and self.y == outro_ator.y:
                self.status = DESTRUIDO
                outro_ator.status = DESTRUIDO
            else:
                limite = intervalo * 2
                d = ((outro_ator.x - self.x) ** 2) + ((outro_ator.y - self.y) ** 2)
                d = math.sqrt(d)
                if d < limite:
                    self.status = DESTRUIDO
                    outro_ator.status = DESTRUIDO


class Obstaculo(Ator):
    pass


class Porco(Ator):
    pass


class DuploLancamentoExcecao(Exception):
    pass


class Passaro(Ator):
    velocidade_escalar = 30

    def __init__(self, x=0, y=0):
        """
        Método de inicialização de pássaro.

        Deve chamar a inicialização de ator. Além disso, deve armazenar a posição inicial e incializar o tempo de
        lançamento e angulo de lançamento

        :param x:
        :param y:
        """
        super().__init__(x, y)
        self._x_inicial = x
        self._y_inicial = y
        self._tempo_de_lancamento = None
        self._angulo_de_lancamento = None  # radianos

    def foi_lancado(self):
        """
        Método que retorna verdaeira se o pássaro já foi lançado e falso caso contrário

        :return: booleano
        """
        if self._tempo_de_lancamento is None and self._angulo_de_lancamento is None:
            return False

        return True

    def colidir_com_chao(self):
        """
        Método que executa lógica de colisão com o chão. Toda vez que y for menor ou igual a 0,
        o status dos Passaro deve ser alterado para destruido, bem como o seu caracter

        """
        if self.y <= 0:
            self.status = DESTRUIDO

    def calcular_posicao(self, tempo):
        """
        Método que cálcula a posição do passaro de acordo com o tempo.

        Antes do lançamento o pássaro deve retornar o valor de sua posição inicial

        Depois do lançamento o pássaro deve calcular de acordo com sua posição inicial, velocidade escalar,
        ângulo de lancamento, gravidade (constante GRAVIDADE) e o tempo do jogo.

        Após a colisão, ou seja, ter seus status destruido, o pássaro deve apenas retornar a última posição calculada.

        :param tempo: tempo de jogo a ser calculada a posição
        :return: posição x, y
        """
        if not self.foi_lancado():
            print('nao lancado')
            return self._x_inicial, self._y_inicial

        if self.status == DESTRUIDO:
            print('destruido')
            return self.x, self.y

        # componente vertical -> y
        # componente horizontal -> x

        tempo = tempo - self._tempo_de_lancamento

        # alcance_horizontal
        self.x = self._x_inicial + math.cos(self._angulo_de_lancamento) * tempo * self.velocidade_escalar

        # vertical considerando subida
        self.y = (self._y_inicial +
             self.velocidade_escalar * tempo * math.sin(self._angulo_de_lancamento) -
             0.5 * GRAVIDADE * tempo ** 2)

        return self.x, self.y

    def lancar(self, angulo, tempo_de_lancamento):
        """
        Lógica que lança o pássaro. Deve armazenar o ângulo e o tempo de lançamento para posteriores cálculo.
        O ângulo é passado em graus e deve ser transformado em radianos

        :param angulo:
        :param tempo_de_lancamento:
        :return:
        """

        self._tempo_de_lancamento = tempo_de_lancamento
        self._angulo_de_lancamento = math.radians(angulo)  # radianos


class PassaroAmarelo(Passaro):
    pass


class PassaroVermelho(Passaro):
    velocidade_escalar = 20