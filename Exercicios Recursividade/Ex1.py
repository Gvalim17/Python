# Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N. 

def fatorial(n: int):
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n - 1)


fat5 = fatorial(5)
print(fat5)
