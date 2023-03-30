# Crie um programa em python que receba um vetor de números reais com 100 elementos. Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor. 

import random
def inverte_vetor(vetor, inicio, fim):
    if inicio < fim:
        vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio]
        inverte_vetor(vetor, inicio + 1, fim - 1)


vetor = random.sample(range(0,100),100)
print("Vetor original:", vetor)
inverte_vetor(vetor, 0, len(vetor) - 1)
print("Vetor invertido:", vetor)
