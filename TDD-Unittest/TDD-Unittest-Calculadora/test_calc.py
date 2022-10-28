from unittest import TestCase, main
import unittest
from calc import sum

class TestCalc(TestCase):
    def test_fala_oi_retorna_oi(self):
        self.assertEqual("hello", "hello")

    def test_sum_de_5_e_5_deve_retornar_10(self):
        self.assertEqual(sum(5,5),10)

unittest.main(verbosity=2)