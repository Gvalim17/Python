class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self,anos):
        for i in range(anos):  
            self.idade += 1
            if self.idade < 21:
                self.altura += (0.5)
            
    def crescer(self,altura):
        self.altura += altura
    
    def engordar(self,peso):
        self.peso += peso
    
    def emagrecer(self,peso):
        self.peso -= peso
            
         
pessoa = Pessoa('Guilherme', 10, 60, 165)
print(vars(pessoa))
pessoa.emagrecer(10)
print(vars(pessoa))
pessoa.envelhecer(20)
print(vars(pessoa))
pessoa.engordar(5)
print(vars(pessoa))
pessoa.crescer(0)
print(vars(pessoa))
