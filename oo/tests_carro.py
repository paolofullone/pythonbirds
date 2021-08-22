from unittest import TestCase
from oo.carro import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self): # obs, para o teste funcionar, o nome deve começar com test, se alterar o nome
        # para 'tes' por exemplo vai retornar um erro.
        motor=Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)