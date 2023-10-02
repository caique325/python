class Pessoa():
    def __init__(self,nome,data_nascimento,cor):
        self.nome = nome
        self.data_nascimento =data_nascimento
        self.cor = cor
        
    def exibir(self):
        print(f'Nome: {self.nome} \nData: {self.data_nascimento} \nCor: {self.cor}')


if __name__ == '__main__':
      
    '''p1 = Pessoa('Caique','02/10/2022','Preta')
    p1.exibir()
    print('\n')
    p2 = Pessoa('Pablo','07/01/2003','Branco')
    p2.exibir()
    print('\n')'''

class Aluno(Pessoa):
    def __init__(self,ra,cod_curso,ano_entrada,campus,periodo,nome,data_nascimento,cor):
        self.ra = ra
        self.cod_curso= cod_curso
        self.ano_entrada = ano_entrada
        self.campus=campus
        self.periodo= periodo
        super().__init__(nome,data_nascimento,cor)

    def exibirAluno(self):
        print(f'Aluno: {self.nome}')
        print(f'Nascimento: {self.data_nascimento} ')
        print(f'RA: {self.ra}')
        print(f'Cod: {self.cod_curso}')
        print(f'Ano: {self.ano_entrada}')
        print(f'Campus: {self.campus}')
        print(f'Periodo: {self.periodo}')
        print('\n')



if __name__ == '__main__':
 
    n = 0
    while (n == 0):
        ra = input('Coloque Seu Ra: ')
        ano_entrada = input('Coloque Sua Data de Entrada: ')
        cod_curso = input('Coloque Seu Codigo: ')
        campus = input('Qual Seu Campus: ')
        nome = input('Coloque Seu nome: ')
        data = input('Coloque sua Data: ')
        cor = input('Coloque sua Cor: ')
        periodo = input('Coloque seu periodo: ')
        print('\n')

        x = Aluno( ra ,cod_curso,ano_entrada,campus,3,nome,data,cor)   
        x.exibirAluno()
        n = input('Voce quer inserir mais? ')
