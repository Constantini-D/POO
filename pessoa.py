
class Compras:

    def __init__(self, produto, valor, quantidade ):
        self.produto = produto
        self.valor = valor
        self.quantidade = quantidade

    def carrinho(self):
        valor = self.valor
        quantidade = self.quantidade
        total = valor*quantidade
        #print(f'o total é: {total}')
        return {total}


from random import randint

class Pessoa:
    ano_atual=2021

    # instancia
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # instancia
    def get_ano_nascimento(self):
        print(self.ano_atual-self.idade)

    # decorator
    @classmethod
    def por_ano_nascimento(cls, ano_nascimento):
        idade = cls.ano_atual-ano_nascimento
        return idade

    @staticmethod
    def gera_id():
        rand = randint(1, 10000)
        return rand

    # getter
    @property
    def nome(self):
        return self._nome

    #setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()




"""p1 = Pessoa('DOUGLAS', 40)
print(p1.nome)


print(Pessoa.gera_id())
p1 = Pessoa.por_ano_nascimento( 1996)

p2 = Pessoa('',25)
p2.get_ano_nascimento()
"""


class Escritor:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome