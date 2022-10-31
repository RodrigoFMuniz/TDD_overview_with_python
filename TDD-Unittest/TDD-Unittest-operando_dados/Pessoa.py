class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.__nome = nome
        self.__sobrenome= sobrenome

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome