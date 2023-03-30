class Conta:
    def __init__(self,saldo):
        self.saldo = saldo
        
class ContaInvestimento(Conta):
    def __init__(self, saldo,taxa_juros):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros
    
    def set_juros(self):
        self.saldo += (self.saldo * self.taxa_juros / 100)
        
conta = ContaInvestimento(1000,10)
conta.set_juros()
conta.set_juros()
conta.set_juros()
conta.set_juros()
conta.set_juros()
print(vars(conta))
























