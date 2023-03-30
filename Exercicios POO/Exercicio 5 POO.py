class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def alterarnome(self, nome_correntista):
        self.nome_correntista = nome_correntista
    
    def deposito(self, valor):
        self.saldo += valor 
    
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else: print('Voce nao tem esse valor me conta')
            


conta = ContaCorrente(13, 'Guilherme', 200)
conta.alterarnome('Guilherme Valim')
print(vars(conta))
conta.saque(300)
print(vars(conta))

