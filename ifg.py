class Aluno:
    """Classe aluno: representa um aluno no ifg"""
    #atributos de classe, pertencente a todos os membros (objetos da classe Aluno)
    nome_ifg = 'Instituto Federal de Goias'
    def __init__(self,nome,ra):
        self.nome = nome
        #self.data_nascimento = data_nacsimento;
        self.ra = ra
        #self.campus = campus;
        #self.entrada = entrada;
        #self.codigo_curso = codigo_curso;
        

        
    #metodo de classe
    

    def exibeAluno(self):
        print(f"Aluno: {self.nome}")
        print(f"RA: {self.ra}")
        #print(f,"Codigo do curso: {self.codigo_curso}");
        #print(f,"Entrada: {self.entrada}");








if __name__ == '__main__':
    aluno = Aluno('Caique',20222010)
    aluno.exibeAluno()

class Sala:
    """Classe sala: Representa uma sala do IFG"""
    def __init__(self,nomeSala,maxAlunos):
        self.nomeSala = nomeSala
        self.maxAlunos = maxAlunos
        self.salaDeAula = []

def insere_aluno(self, aluno):
    if len(self.salaDeAula < self.maxAlunos):
        self.salaDeAula.append(aluno)
    else:
        print("excedeu a quantidade")

def exibeSala(self):
    n =1 
    for Aluno in self.salaDeAula:
        print(f'{n} -{Aluno.exibeSala()}')
        n = n + 1

