import calendar

class Pessoa():
    def __init__(self,nome,data_nascimento,id):
        self.nome = nome
        self.data_nascimento =data_nascimento
        self.id = id


        
    def exibirAluno(self):
        print(f'Nome: {self.nome} \nData: {self.data_nascimento} \nCor: {self.cor}')


class Aluno(Pessoa):
    def __init__(self,ra,campus,codigo_curso,ano_entrada,nome,data_nascimento,id,idade):
        self.ra = ra
        self.ano_entrada = ano_entrada
        self.campus=campus
        self.codigo_curso = codigo_curso 
        self.idade = idade


        super().__init__(nome,data_nascimento,id)
    def exibirAluno(self):
        return f'Nome: {self.nome} RA: {self.ra} '
        
        
class Sala(Aluno):
    def __init__(self,nomeSala,maxAlunos):
        self.nomeSala = nomeSala
        self.maxAlunos = maxAlunos
        self.listaAluno = []
        

    def insereAluno(self,aluno):

        if len(self.listaAluno) < self.maxAlunos and not aluno in self.listaAluno and aluno.idade >16:
            self.listaAluno.append(aluno)
        

    def removeAluno(self,aluno):
        self.listaAluno.pop(aluno)

    def exibirSala(self):
        n = 1
        for aluno in self.listaAluno:
            print(f'{n} - {aluno.exibirAluno()}')
            n = n + 1



if __name__ == '__main__':
    nome=['','','','']
    data_nascimento=['','','','']
    idade=['','','','']
    for i in range(3):
        nome[i] = input(f'digite O Nome Do {i+1} Aluno: ')
        data = int(input(f'Coloque Data de Nasicmento do {i+1} aluno: '))
        mes = int(input(f'Coloque o mes de nascimento do {i+1} aluno: '))
        ano = int(input(f'Coloque o ano de nascimento do {i+1} aluno: '))
        while(data <= 0) or (data >= 32) or (mes <= 0) or (mes >= 13) or (ano > 2023):
            print('Digite uma data valida: ')
            data = int(input('Coloque sua Data de Nasicmento: '))
            mes = int(input('Coloque o mes de nascimento: '))
            ano = int(input('Coloque o ano de nascimento: '))
        
        idade[i] =  2023 - ano
        data  = str(data)
        mes  = str(mes)
        ano  = str(ano)
        
        data_nascimento[i] = str(data  + '/' + mes  + '/' + ano)
        print(data_nascimento[i])
        
    POO = Sala('POO',3)
    estudante = Aluno(20222010,'IFG',20102015,2023,nome[0],data_nascimento[0],12345,idade[0])
    POO.insereAluno(estudante)
    estudante = Aluno(20222010,'IFG',20102015,2023,nome[1],data_nascimento[1],12345,idade[1])
    POO.insereAluno(estudante)
    estudante = Aluno(20222010,'IFG',20102015,2023,nome[2],data_nascimento[1],12345,idade[2])
    POO.insereAluno(estudante)
  
    
    #parametro 0 para remover o primeiro aluno da lista 
    POO.removeAluno(0)
    print('Exibindo Alunos da Sala')
    POO.exibirSala()
