class Robo:
    def __init__(self,nome,fome,saude,idade):
        self.nome = str(nome)
        self.fome = str (fome)
        self.saude = str (saude)
        self.idade = int (idade)

    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        self.nome
    def setSaude(self, saude):
        self.saude = saude 
    def getSaude(self):
        self.saude
    def setIdade(self, idade):
        self.idade = idade 
    def getIdade(self):
        self.idade
    def alterar(self):
        self.getSaude()
robo = Robo('Einsten','muita','regular',23)
print(robo.alterar())
print(vars(robo))