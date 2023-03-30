# Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente. 

def num(n):
    if n == 0:
        return 
    else:
        if n % 2 == 0:
            print(n)
        return num(n-1)

    
num(24)