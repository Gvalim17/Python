# Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N. 

def somatorio(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return (n) + somatorio(n - 1)

soma = somatorio(12)
print(soma)
    