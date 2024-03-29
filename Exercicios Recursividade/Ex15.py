# A função fatorial duplo é definida como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15 Faça uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número.

def fatorial(n: int):
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n - 2)


fat5 = fatorial(5)
print(fat5)