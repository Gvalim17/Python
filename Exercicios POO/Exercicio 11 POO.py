class Carro:
    
    def __init__(self,consumo):
        self.consumo = consumo
        self.nivel_combustivel = 0
        
    def andar(self,percorre):
        valor = percorre / self.consumo
        self.nivel_combustivel -= valor
    
    def get_gasolina(self):
        return self.nivel_combustivel
    
    def set_gasolina(self,abastecer):
         self.nivel_combustivel += abastecer
        
car = Carro(15)
car.set_gasolina(20)
print(vars(car))
car.andar(100)
print(round(car.get_gasolina(),2))