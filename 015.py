from tkinter import N


class Disciplina:
    def __init__ (self, nome, coddispl):
        self.nome = nome
        self.coddiscipl = coddispl
        self.nota = 0 
    def disciplinas(self):
        print('Acesso a lista de disciplinas pelo codigo:', self.coddisipl)
    def getdiscipl(self):
        print('nota total das disciplinas', self.nota)
    def setdiscipl (self, n):
        self.nota = n
        print ('nota atual da media das disciplinas',self.nota)
    def mostradescipl (self):
        print (f'A disciplina {self.nome} com o codigo: {self.coddiscipl}')
disciplina = Disciplina ('TI',3869)
disciplina.mostradescipl()
disciplina.disciplinas()
disciplina.getdiscipl()
disciplina.setdiscipl(10)