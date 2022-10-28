from unittest import TestCase, main
import unittest
from calc import sum

class TestCalc(TestCase):
    def test_fala_oi_retorna_oi(self):
        self.assertEqual("hello", "hello")

    def test_sum_de_5_e_5_deve_retornar_10(self):
        self.assertEqual(sum(5,5),10)
    
    def test_soma_de_diversas_entradas_aleatorias(self):
        x_y_saidas = [
            (1,2,3),
            (1,5,6),
            (32,20,52),
            (1112,2,1114),
            (67,-7,60),
            (39,-43,-5),
        ]

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x,y,s = x_y_saida
                self.assertEqual(sum(x,y),s)

unittest.main(verbosity=2)