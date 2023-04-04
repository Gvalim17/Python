#1.Faça um Programa que mostre a mensagem "Alo mundo" na tela.
#print("Alo, Mundo!")

#2.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
#y = int(input("Insira um numero: "))
#print(f"O numero inserido foi: {y}")

#3. Faça um Programa que peça dois números e imprima a soma.
#x = float(input('Insira um numero: '))
#y = float(input('Insira outro numero: '))
#print(f'A soma dos numeros escolidos e', {x + y})

#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média
#nota1 = float(input('Informe a primeira nota do Aluno: '))
#nota2 = float(input('Informe a segunda nota do Aluno: '))
#nota3 = float(input('Informe a terceira nota do Aluno: '))
#nota4 = float(input('Informe a quarta nota do Aluno: '))
#print(f'A sua media ficou em',{(nota1 + nota2 + nota3 + nota4) / 4})

#5. Faça um Programa que converta metros para centímetros.
#metros = float(input('Informe o valor em metros: '))
#print (f'O valor em centimetros eh',{metros * 100})

#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
#raio = float(input('Informe o raio do circulo: '))
#print(f'A area do circulo e: ',{3.14 * raio**2}) 

#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
#lado = int(input('Informe o lado do quadrado: '))
#print(f'A area do quadrado e: {lado * lado}, o seu dobro e {(lado * lado) * 2}')

#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
#hora = float(input('Quanto voce ganha por hora? '))
#mes = float(input('Quantas horas voce trabalha por mes? '))
#sal = hora * mes
#print(f'Seu salario no final do mes e: R${sal}')

#9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
#temp = float(input('Informe a temperatura em Fahrenheit: '))
#c = 5 * ((temp - 32)/9)
#print(f'A temperatura informada transformada em Celsius e {c:.2f}')

#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#temp = float(input('Informe a temperatura em Celsius: '))
#F = temp * 1.8 + 32
#print(f'A temperatura informada transformada em Fahrenheit e {F:.2f}')

#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    #o produto do dobro do primeiro com metade do segundo .
    #a soma do triplo do primeiro com o terceiro.
    #o terceiro elevado ao cubo.
#num1 = int(input('Digite o primeiro número inteiro:  '))
#num2 = int(input('Digite o segundo número inteiro: '))
#num3 = float(input('Digite o primeiro número real: '))
#print(f'o produto do dobro do primeiro com metade do segundo = {(num1*2) + (num2/2)}')
#print(f'a soma do triplo do primeiro com o terceiro. = {(num1*3)+num3}')
#print(f'o terceiro elevado ao cubo = {num3**3}')

#12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
#alt = float(input('Informe sua altura: '))
#ideal = (72.7*alt) - 58
#print(f'Seu peso ideal e: {ideal :.2f}')

#13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas
#    a.Para homens: (72.7*h) - 58
#    b.Para mulheres: (62.1*h) - 44.7

#gen = input('Informe seu genero (M) ou (F): ')
#alt = float(input('Informe sua altura: '))
#idealm = (72.7*alt) - 58
#idealf = (62.1*alt) - 44.7
#if gen == 'M':
#    print(f'Seu peso ideal e: {idealm :.2f}')
#else:
#    print(f'Seu peso ideal e: {idealf :.2f}')

#14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

#peso = float(input('Informe o peso de peixe que esta trazendo: '))
#excesso = peso - 50
#if peso > 50:
#    print('Voce esta trazendo mais que o permitido! \n\n'f'Pagara um adicional de R$ 4,00 por quilo excedente = R$ {excesso * 4 :.2f}')
#else:
#    print('\n O peso de peixe que esta sendo transportado esta dentro dos padroes. Voce pode seguir!')
    
#15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

#hora = float(input('Quanto voce ganha por hora? '))
#mes = float(input('Quantas horas voce trabalha por mes? '))
#ir = (hora*mes) * 0.011 
#ins = (hora*mes) * 0.008
#sind = (hora*mes) * 0.005
#print(f'Seu salario bruto e: R$ {hora*mes}')
#print(f'Voce paga R$ {ir} de Imposto de Renda')
#print(f'Voce paga R$ {ins} ao INSS')
#print(f'Voce paga R$ {sind} ao Sindicato')
#print(f'Seu salario liquido e: R$ {hora*mes-ir-ins-sind}')

#16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#tam = float(input('Informe a area em metros quadrados a ser pintada: '))
#litros = tam / 3
#latas = int(litros/18)
#if litros % 18 != 0:
#    latas += 1
#print(f'Quantidade de litros de tinta necessaria: {litros}') 
#print(f'Quantidade de latas necessarias: {latas}') 
#print(f'Valor total a pagar: R$ {latas*80}') 

#17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#tam = float(input('Informe a quantidade a ser pintada: '))
#litros = tam / 6 * 1.1
#galoes = litros / 3.6
#latas = litros / 18
#if (litros % 18 !=0):
#    latas += 1
#if (litros % 3.6 !=0):
#    galoes += 1
#mixlatas = litros/18
#mixgaloes = litros - (mixlatas * 18) / 3.6
#if ((litros - (mixlatas * 18)% 3.6 !=0)):
#    mixgaloes += 1
#print('Latas ', latas, '- Valor: ', latas * 80)
#print('Galoes ', galoes, '- Valor: ', galoes * 25)
#print('Latas ', mixlatas, '- Valor: ', mixgaloes, ' - Valor: ',(mixlatas*80)+(mixgaloes*25))

#18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

#tam = float(input('Digite o tamanho do arquivo em (MB): '))
#vel = float(input('Digite a velocidade da internet em (MBps): '))
#bits = tam * 1024 * 1024 * 8
#tseg = bits / (vel * 1024 * 1024)
#tmin = tseg / 60 
#print(f'O tempo do dowload sera: {tmin :.1f} minutos')