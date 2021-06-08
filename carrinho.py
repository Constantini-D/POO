class Carrinho:

    def __init__(self):
        self.produtos = []

    def adicionar_produtos(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.atribuicao)

    def soma(self):
        total = 0
        for produto in self.produtos:
            total += produto.atribuicao
        return print(total)

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor