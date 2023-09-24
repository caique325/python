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
        #print(f"Aluno: {self.nome}")
        #print(f"RA: {self.ra}")
        #print(f,"Codigo do curso: {self.codigo_curso}");
        #print(f,"Entrada: {self.entrada}");
        return f'Nome: {self.nome} \t RA: {self.ra}'



class Sala:
    """Classe sala: Representa uma sala do IFG"""
    def __init__(self,nomeSala,maxAlunos):
        self.nomeSala = nomeSala
        self.maxAlunos = maxAlunos
        self.salaDeAula = []

    def insere_aluno(self, aluno):
        if len(self.salaDeAula) < self.maxAlunos:
            self.salaDeAula.append(aluno)
        else:
            print("excedeu a quantidade")

    def exibeSala(self):
        n = 1 
        for aluno in self.salaDeAula:
            print(f'{n} - {aluno.exibeAluno()}')
            n = n + 1




if __name__== '__main__':
    ifg = Sala('ifg',5)
    aluno = Aluno('Caique Magalhaes',20222010000)
    ifg.insere_aluno(aluno)
    aluno = Aluno('Pablo Herrison',20222010000)
    ifg.insere_aluno(aluno)
    aluno = Aluno('Andre Fiusa',20222010000)
    ifg.insere_aluno(aluno)
    aluno = Aluno('Tiago Curtinhas',20222010000)
    ifg.insere_aluno(aluno)
    aluno = Aluno('Andre Ciclo',20222010000)
    ifg.insere_aluno(aluno)

    ifg.exibeSala()
