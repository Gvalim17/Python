class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def mudar_lados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def rretangulo(self):
        return self.comprimento, self.largura
    
    def area(self):
        return self.comprimento * self.largura
    
    def perimetro(self):
        return (self.comprimento + self.largura) * 2
        
comprimento = float(input('Informe o comprimento: '))
largura = float(input('Informe a largura: '))
retangulo = Retangulo(comprimento,largura)
print(retangulo.rretangulo())
print('Area  = ', retangulo.area())
print('Perimetro  = ', retangulo.perimetro())
