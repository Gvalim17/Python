import random
import statistics
from functools import reduce

# 1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

# vet = [1,2,3,4,5]
# print(vet)

# 2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

# vet = [1,2,3,4,5,6,7,8,9,10]
# vet.reverse()
# print(vet)

# 3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

# notas = [7.0,8.5,6.4,10]
# media = (sum(notas)) / len(notas)
# print(notas)
# print(round(media,2))

# 4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

# vetor = []
# vogais = "AEIOU"
# for i in range(10):
#     letras = (input("digite os caracteries: ").upper())
#     vetor.append(letras)

# num_consoantes = 0
# consoantes = ""

# for letras in vetor:
#     if letras not in vogais:
#         num_consoantes += 1
#         consoantes += letras

# print(f"A lista tem {num_consoantes} consoantes")
# print(consoantes)

# 5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# vet_par = []
# vet_impar = []
# for numero in numeros:
#     if numero % 2 == 0:
#         vet_par.append(numero)
#     else:
#         vet_impar.append(numero)
# print(vet_par)
# print(vet_impar)

# 6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

# medias = []
# media_boa = []
# qtde_alunos_aprovados = 0

# for i in range(5):
#     notas = []
#     print('-=-=-'*7)
#     for j in range(4):
#         nota = float(input(f'Informe a nota {j+1} do {i+1} Aluno: '))
#         notas.append(nota)
# media = sum(notas) / len(notas) Calculo da media usando (Sum e Len)
#     media = statistics.mean(notas) # Calculo da media usando bliblioteca statistic
#     medias.append(media)
#     if media >= 7.0:
#         qtde_alunos_aprovados += 1
#         media_boa.append(media)
# print(f'Um total de - {qtde_alunos_aprovados} - aluno(s) tiveram media igual ou maior que 7')
# print(f'As medias foram - {media_boa} -')


# 7 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

# vet_num_int = [1,2,3,4,5]
# soma = sum(vet_num_int)
# multiplicacao = reduce(lambda x,y: x + y**2, vet_num_int) # Lambda faz a (multiplicacao) cumulativa dos elementos da lista.
# print(vet_num_int)
# print(soma)
# print(multiplicacao)

# 8 - Faça um Programa que peça a altura e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

# idades = []
# alturas = []
# for i in range(5):
#     idade = int(input(f'Informe a {i+1} idade: '))
#     altura = float(input(f'Informe a {i+1} altura: '))
#     idades.append(idade)
#     alturas.append(altura)

# Print idades e altura e seus reversos
# print(idades)
# print(alturas)
# idades.reverse()
# alturas.reverse()
# print(idades)
# print(alturas)

# Print idades e altura e seus reversos com for
# for idade in reversed(idades):
#     print(idade)
# for altura in reversed(alturas):
#     print(idade,altura)


# 9 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

# vetorA = []
# for i in range(10):
#     try:
#         vetor = int(input(f'Informe os numeros {i+1}°: '))
#     except ValueError:
#         vetor = 1
#     vetorA.append(vetor)

# soma_quadrados = reduce(lambda x,y: x + y**2, vetorA)
# print('A soma dos quadrados dos elementos do vetor é:', soma_quadrados)


# 10 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

# Metodo usando randint e for
# vet1 = []
# vet2 = []
# vet3 = []

# for i in range(10):
#     vet1.append(random.randint(0, 100))
#     vet2.append(random.randint(0, 100))

# Outra forma de fazer esse range e com o sample da biblioteca random
# vetor1 = random.sample(range(1, 50), 10)
# vetor2 = random.sample(range(50, 100), 10)
# vetor3= []

# O for a,b in zip faz com que o for ande pelos dois vetores com cada variavel assumindo um valor.
# for a, b in zip(vetor1, vetor2):
#     vetor3.append(a)
#     vetor3.append(b)

# print(vetor1)
# print(vetor2)
# print(vetor3)

# 11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

# vetor1 = random.sample(range(1, 50), 10)
# vetor2 = random.sample(range(50, 100), 10)
# vetor3 = random.sample(range(100, 150), 10)
# vetor4 = []

# for a, b, c in zip(vetor1,vetor2,vetor3):
#     vetor4.append(a)
#     vetor4.append(b)
#     vetor4.append(c)

# print(vetor1)
# print(vetor2)
# print(vetor3)
# print(vetor4)

# 12 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

# alunos = []
# alturas = []
# for i in range(3):
#     while True:
#         try:
#             idade = int(input(f"Informe a idade do aluno: "))
#             altura = float(input(f"Informe a altura do aluno: "))
#             if idade < 1 or altura < 0: 
#                 raise ValueError
#             break
#         except ValueError:
#             print('Digite uma altura ou idade valida.')

#     alunos.append((idade,altura))
#     alturas.append(altura)

# media_alturas = sum(alturas) / len(alturas)

# qtde_alunos = 0
# for idade, altura in alunos:
#     if idade > 13 and altura < media_alturas:
#         qtde_alunos += 1
# print(f'{qtde_alunos} Aluno(s) de mais de 13 anos que tem altura menor que a media')


# 13 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

# mes_temperaturas = [(1, 27.5), (2, 27.8), (3, 27.7), (4, 27.0), (5, 26.1), (6, 24.7), (7, 24.3), (8, 24.8), (9, 25.7), (10, 26.5), (11, 26.9), (12, 27.3)]
# temperatura = []
# for mes,temp in mes_temperaturas:
#     temperatura.append(temp)
# media_temperaturas = sum(temperatura) / len(temperatura)
# temp_acima_media = []
# for mes,temp in mes_temperaturas:
#     if temp > media_temperaturas:
#         temp_acima_media.append((mes,temp))

# print('Temperaturas acima da média',round(media_temperaturas,1),':')
# for mes, temp in temp_acima_media:
#     print(f"Mês {mes}: {temp}")


    