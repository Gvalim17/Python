class BombaCombustivel:
    def __init__(self, tipocombustivel, valorlitro, quantidadecombustivel):
        
        self.tipocombustivel = tipocombustivel
        self.valorlitro = valorlitro
        self.quantidadecombustivel = quantidadecombustivel

    def setvalor(self, valorlitro):
        self.valorlitro = valorlitro

    def setcombustivel(self, tipocombustivel):
        self.tipocombustivel = tipocombustivel

    def setquantidade_combustivel(self, quantidadecombustivel):
        self.quantidadecombustivel = quantidadecombustivel

    def abastecer_porvalor(self, valor):
        temp = valor/self.valorlitro
        self.setquantidade_combustivel(self.quantidadecombustivel - temp)
        return print('Com R$',float(valor),'voce paga por',temp,'litros de',self.tipocombustivel)  

    def abastecer_porlitro(self, qtde):
        temp2 = qtde * self.valorlitro
        self.setquantidade_combustivel(self.quantidadecombustivel - qtde)
        return print(float(qtde),'Litros de',self.tipocombustivel,'custa R$',float(temp2))  


bomba = BombaCombustivel("Alcool", 2, 500)
print(vars(bomba))
print()
bomba.abastecer_porvalor(80)
print()
bomba.abastecer_porlitro(40)
print()
bomba.setvalor(4)
print()
bomba.abastecer_porvalor(80)
print()
print(vars(bomba))

