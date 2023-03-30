class Cliente:
    def __init__(self, nome,email,plano):
        self.nome = nome
        self.email = email
        self.lista_plano = ["basic","premium"]
        if plano in self.lista_plano:
            self.plano = plano
        else:
            raise Exception('Plano invalido')
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano
        else:
            print('Plano Invalido')
        
    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print('Faca um upgrade para ver o filme')
        else:
            print('Plano invalido')
            
        
cliente = Cliente("Guilherme","Guilherme.v.varaujo@hotmail.com", "basic")
print(vars(cliente))
print(cliente.plano)
cliente.ver_filme('John Wick', 'premium')
cliente.mudar_plano('premium')
print(cliente.plano)
cliente.ver_filme('John Wick', 'premium')