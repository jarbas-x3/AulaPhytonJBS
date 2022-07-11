class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, idade):
        if (self.idade<21):
            self.altura += 0.5
            self.idade += idade
        
        self.idade += idade
    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura
    
    def mostraPessoa(self):
        print(f'Nome: {self.nome}, idade: {self.idade} anos, peso: {self.peso}kg, altura: {self.altura}cm')
    
ana = Pessoa('Ana', 19, 54, 163)
ana.mostraPessoa()


ana.emagrecer(3)
ana.mostraPessoa()

