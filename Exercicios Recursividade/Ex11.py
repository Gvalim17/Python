# Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente. 

def num(n):
    if n == 0:
        return 
    else:
        num(n-1)
        print(n)
num(10)
    