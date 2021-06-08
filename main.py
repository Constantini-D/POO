class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor.tittle()

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        self.__idade = valor

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        self.__altura = valor

    def imprimir(self):
        return(print(f'Nome:{self.nome}, Idade: {self.idade}, Altura: {self.altura}'))

pessoa1=Pessoa('douglas', 24, 1.80)

pessoa1.imprimir()















'''"""

class Produto:
    atribuicao = 1

    def __init__(self, arg):
        self.atribuicao = arg



print('Valores são passados para o "atribuicao", mas não são atribuidos como o novo valor dele ')
obj1 = Produto(2)
obj2 = Produto(10)
print(Produto.atribuicao)
print(obj1.atribuicao)
print(obj2.atribuicao)

print('o valor é passados para a instancia do obj1, mas este não é guardado na variavel da classe  ')
obj1.atribuicao = 22222222
print(Produto.atribuicao)
print(obj1.atribuicao)
print(obj2.atribuicao)


print('Já nesse, o valor é guardado a variavel "atribuicao" ')
Produto.atribuicao = 1234
print(Produto.atribuicao)
print(obj1.atribuicao)
print(obj2.atribuicao)


print('\n \n')
p = Produto
print(p.atribuicao)













class Produto:

    def metodo(self, arg):
        print(arg)


p = Produto
p.metodo(1)




class Produto:

    def __init__(self, arg):
        self.arg = arg

    def metodo(self):
        print(self.arg)

class T:

    @classmethod
    def teste(cls, teste):
        cls.teste = teste
        print(teste)

p = Produto('Oii')
p.metodo()

u = T
u.teste('oi')
"""'''

