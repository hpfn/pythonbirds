"""VocÊ deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classe:

1) Motor
2) Direção

O Motor trá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes attributos:

1) Attr de dado velocidade
2) Method acelear, que deverá incrementar a velocidade de
   uma unidade
3) Method frear que deverá decrementar a velocidade em duas
   unidades.

A Direção terá a responsabilidede de controlar a direção.
  Ela oferacerá os seguintes attrs:

1) Valor da direção com valores possíveis: Norte, Sul, Leste
   Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda

  N
O   L
  S

  Exemplo:
  >>> # Testando Motor
  >>> motor = Motor()
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
  >>> # Testando Direcao
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
  >>>
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


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)
        # if self.velocidade > 2:
        #     self.velocidade -= 2
        # else:
        #     self.velocidade = 0

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita = {
        NORTE: LESTE,
        LESTE: SUL,
        SUL: OESTE,
        OESTE: NORTE
    }
    rotacao_a_esquerda = {
        NORTE: OESTE,
        OESTE: SUL,
        SUL: LESTE,
        LESTE:NORTE
    }
    
    def __init__(self):
        # self.direcao_valores = ['Norte', 'Leste', 'Sul', 'Oeste']
        # self.valor = 'Norte'
        self.valor = NORTE

    def girar_a_direita(self):
        # direcao_atual = self.direcao_valores.index(self.valor)
        # if self.valor == 'Oeste':
        #     direcao_atual = 0
        # else:
        #     direcao_atual += 1
        #
        # self.valor = self.direcao_valores[direcao_atual]
        self.valor = self.rotacao_a_direita[self.valor]

    def girar_a_esquerda(self):
        # direcao_atual = self.direcao_valores.index(self.valor)
        # if self.valor == 'Norte':
        #     direcao_atual = 3
        # else:
        #     direcao_atual -= 1
        #
        # self.valor = self.direcao_valores[direcao_atual]
        self.valor = self.rotacao_a_esquerda[self.valor]


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()