class Funcionario():

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, porcentagemDeAumento=0):
        self.salario += self.salario * (porcentagemDeAumento)/100


Func = Funcionario("Jose", 1200)
print("Nome: ", Func.getNome(), ", Salario", Func.getSalario())
Func.aumentarSalario(10)
print("Nome: ", Func.getNome(), ", Salario", Func.getSalario())
