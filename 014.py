class Curso:
    def __init__(self, codcurso, nomecurso, codturma, coddisciplina):
        self.codcurso = codcurso
        self.nomecurso = nomecurso
        self.codturma = codturma
        self.coddisciplina = coddisciplina
    def montacurso(self, codcurso):
        self.codcurso = codcurso
    def organizarcurso(self, codturma):
        self.codturma = codturma
    def mostracurso(self, mostracurso):
        print(f'Codcurso; {self.codcurso}, Nome curso: {self.nomecurso}, codturma: {self.codturma}, coddisciplina: {self.coddisciplina}')
curso = Curso(1, 'TI= programação', 2, 1)
curso.mostracurso()
curso.montacurso(2)
curso.organizarcurso(4)
curso.mostracurso