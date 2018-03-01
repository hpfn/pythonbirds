from unittest import TestCase
from oo.carro import Motor, Direcao, Carro


class CarroTestCase(TestCase):
    def setUp(self):
        self.motor = Motor()
        self.direcao = Direcao()

    def test_velocidade_inicial(self):
        self.assertEqual(0, self.motor.velocidade)

    def test_acelerar(self):
        self.motor.acelerar()
        self.assertEqual(1, self.motor.velocidade)

    def test_frear(self):
        self.motor.acelerar()
        self.motor.frear()
        self.assertEqual(0, self.motor.velocidade)

    def test_direcao_inicial(self):
        self.assertEqual('Norte', self.direcao.valor)

    def test_direcao_direita(self):
        rumo = list(self.direcao.rotacao_a_direita.values())

        with self.subTest():
            for i in rumo:
                self.direcao.girar_a_direita()
                self.assertEqual(i, self.direcao.valor)

    def test_direcao_esquerda(self):
        rumo = list(self.direcao.rotacao_a_esquerda.values())

        with self.subTest():
            for i in rumo:
                self.direcao.girar_a_esquerda()
                self.assertEqual(i, self.direcao.valor)
















