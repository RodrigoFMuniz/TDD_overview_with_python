'''
class Pessoa:
    __init__
        nome:str
        sobrenome:str
        dados_obtidos:bool

    API:
        obter_todos_os_dados -> method
            ok
            404
'''

import unittest 
from Pessoa import Pessoa

class TestPessoa(unittest.TestCase):

    def setUp(self):
        self.p1 = Pessoa('Rodrigo','Muniz')

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome,"Rodrigo")


if __name__=='__main__':
    unittest.main(verbosity=2)