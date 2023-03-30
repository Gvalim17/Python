# Faça uma função recursiva que permita somar os elementos de um vetor de inteiros. 

def soma_vetor(vetor, n):
    if n == 0:
        return vetor[0]
    else:
        return vetor[n] + soma_vetor(vetor, n - 1)

vetor = [1, 2, 3, 4, 5, 6, 7]
soma_total = soma_vetor(vetor, len(vetor) - 1)
print(soma_total)  
