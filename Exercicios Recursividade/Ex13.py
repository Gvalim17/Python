# Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente. 

def num(n):
    if n == 0:
        return 
    else:
        num(n-1)
        if n % 2 == 0:
            print(n)

    
num(25)
    