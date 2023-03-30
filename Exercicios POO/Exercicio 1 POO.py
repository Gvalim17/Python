class Bola:
    def __init__(self, cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocar_cor(self, cor):
        self.cor = cor
    
    def mostrar_cor(self):
        return self.cor
        
bola1 = Bola("Preto","25","Polietileno")
print(bola1.circunferencia)
print(bola1.material)
print(bola1.mostrar_cor())
bola1.trocar_cor("Azul")
print(bola1.mostrar_cor())