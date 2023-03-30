# Crie um programa em python, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule kn . Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função. 

def potencia_kn(k,n):
    if n == 1:
        return k
    elif n == 0:
        return 1
    return (k) * potencia_kn(k,n - 1)

pot = potencia_kn(2,5)
print(pot)
