class Tamagoshi():

    def __init__(self, nome, fome, saude, idade):
        self.setNome(nome)
        self.setFome(fome)
        self.setSaude(saude)
        self.setIdade(idade)

    def setNome(self, nome):
        self.nome = nome

    def setFome(self, fome):
        self.fome = fome

    def setSaude(self, saude):
        self.saude = saude

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude

    def getIdade(self):
        return self.idade

    def humor(self):
        return self.getFome() * self.getSaude()

    def alimenta(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100.0)

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.saude += self.saude * (quantidade / 100.0)
            
    def str(self):
        return ("Nome: " + str(self.getNome()) + ", Fome: " + str(self.getFome()) + ", Saude: " + str(self.getSaude()) + ", Idade: " + str(self.getIdade()))


tamagoshi = Tamagoshi("Tamagoshi", 5, 5, 5)
print(tamagoshi.humor())
tamagoshi.alimenta(30)
print(tamagoshi.humor())
tamagoshi.brincar(20)
print(tamagoshi.humor())
print(tamagoshi.str())
