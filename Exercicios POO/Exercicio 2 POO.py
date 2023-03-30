class Quadrado:
    def __init__(self, tam_lado):
        self.tam_lado = tam_lado
    
    def mudar_lado(self, tam_lado):
        self.tam_lado = tam_lado
    
    def rlado(self):
        return self.tam_lado
    
    def area(self):
        return self.tam_lado * self.tam_lado
    
quadrado = Quadrado(4)
print(quadrado.rlado())
quadrado.mudar_lado(5)
print(quadrado.rlado())
print(quadrado.area())