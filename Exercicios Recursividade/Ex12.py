#  Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente. 

def num(n):
    if n == 0:
        return 
    else:
        print(n)
        num(n-1)
num(10)
    
