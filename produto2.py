class Produto:
    
    def __init__(self,nome,tipo_unidade,quantidade,preco):

        self.nome = nome
        self.tipo_unidade = tipo_unidade
        self.quantidade = quantidade
        self._preco = preco

    @property # getter
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self,v1):
        if isinstance(v1,str):
            valor = v1.replace(' ','')
            valor = valor.replace('.','')
            valor = valor.replace(',','.')
            valor = float(valor.replace('R$',''))
            self._preco = valor
        else:
            self._preco = v1

    def exibirProdutos(self):
        print(f'Produto: {self.nome}')
        print(f'quantidade: {self.quantidade} {self.tipo_unidade}')
        print(f'Valor: R$ {self.preco}')

    def venda(self, quantidade):
        print(f'Produto {self.nome} x {quantidade} = { self.preco*quantidade}')




if __name__ == '__main__':

    prod1 = Produto('Coca-Cola','ml',600,6.00)
    prod1.exibirProdutos()
    prod1.venda(2)
    prod1.preco = 'R$ 6,50' 
    prod1.venda(2)
    print(f'{prod1._preco}')
