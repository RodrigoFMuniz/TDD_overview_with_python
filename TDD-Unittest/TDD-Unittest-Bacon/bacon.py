"""
1- Receber um número inteiro
2- Quero saber se o número é multiplo de 3 e 5: retorna bacon com ovos
3- Saber se o número é multiplo somente de 3: Retorna bacon
4- Saber se o número é multiplo somente de 5: Retorna ovos
5- Saber se o número não é multiplo de 3 e 5: Retorna passa necessidade
"""

def bacon(num):
    assert isinstance(num, (int)), "Param must be an integer"
    if num%3 == 0 and num%5 == 0:
        return "Bacon com ovos"

    if num%3 == 0:
        return "Bacon"

    if num%5 == 0:
        return "Ovos"
    
    else:
        return "Passa necessidade"
