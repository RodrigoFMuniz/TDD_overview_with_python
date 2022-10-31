"""
1- Receber um número inteiro
2- Quero saber se o número é multiplo de 3 e 5: retorna bacon com ovos
3- Saber se o número é multiplo somente de 3: Retorna bacon
4- Saber se o número é multiplo somente de 5: Retorna ovos
5- Saber se o número não é multiplo de 3 e 5: Retorna passa necessidade

Usando TDD:

Desenvolvimento orientado a testes
Roadmap

1- Criar o teste e vê-lo falhar - RED
2- Criar o código e ver teste passar - GREEN
3- Refatorar o código / Melhorar o código.

"""

from unittest import TestCase, main
from bacon import bacon

class TestBacon(TestCase):
    def test_se_numero_eh_inteiro(self):
        with self.assertRaises(AssertionError):
            bacon("0")
    
    def test_bacon_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15,30,45,60)
        saida = "Bacon com ovos"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon(entrada), saida, msg="Não são iguais")
    
    def test_bacon_deve_retornar_bacon_se_entrada_for_somente_multiplo_de_3(self):
        entradas = (3,6,9,12)
        saida = "Bacon"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon(entrada), saida, msg="Não são iguais")
    
    def test_bacon_deve_retornar_ovos_se_entrada_for_somente_multiplo_de_5(self):
        entradas = (5,10,20,25)
        saida = "Ovos"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon(entrada), saida, msg="Não são iguais")
    
    def test_bacon_deve_retornar_passa_necessidade_se_entrada_nao_for_multiplo_de_3_e_de_5(self):
        entradas = (2,5, 7,31,11)
        saida = "Passa necessidade"
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon(entrada), saida, msg="É múltiplo de 3, ou 5")
    



main(verbosity=2)