#15 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 
# (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

import statistics

notas = []
notas_boas = 0
notas_ruins = 0
nota = 0

while nota != -1:
    try:
        nota = float(input('Informe as notas (sair = - 1): '))
        if nota == -1:
            break
        if nota < 0 or nota > 10:
            print('Valor invalido. Insira um numero valido!')
            continue         
        notas.append(nota)
        if nota >= 7:
            notas_boas += 1
        else:
            notas_ruins += 1
    except ValueError:
        print('Valor invalido. Insira um numero valido!')
        

print('\n-=-=-=- Saida de dados -=-=-=-\n')

qtde_notas = len(notas)
print(f"Foram um total de {qtde_notas} notas")
print('-=-=-=-'*10)

print("Valores na ordem que foram informados")
print(notas)
print('-=-=-=-'*10)
print("Valores na ordem inversa e um abaixo do outro:")
for i in reversed(notas):
    print(i)
print('-=-=-=-'*10)
soma = sum(notas)
print("A soma dos valores da lista notas: ",soma)
print('-=-=-=-'*10)
media = statistics.mean(notas)
print("A media dos valores da lista Notas: ",round(media,2))
print('-=-=-=-'*10)
print("O total de valores acima da media e: ",notas_boas)
print('-=-=-=-'*10)
print("O total de valores abaixo de 7 e: ",notas_ruins)

print("\n-=-=-=- Fim do Programa -=-=-=-")

    
    