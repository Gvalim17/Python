# Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321 

# def inverte(num, aux=0):
#     if num < 10:
#         return aux + num
#     aux = aux * 10 + num % 10 * 10
#     return inverte(num // 10, aux)

# if __name__ == "__main__":
#     inverte_numero = inverte(102)
#     print(inverte_numero)

# Chat GPT
def inverte_numero(n):
    if n < 10:
        return n
    else:
        ultimo_digito = n % 10
        resto_do_numero = n // 10
        novo_numero = inverte_numero(resto_do_numero)
        numero_invertido = (ultimo_digito * (10 ** len(str(resto_do_numero)))) + novo_numero
        return numero_invertido

if __name__ == "__main__":
    inverte = inverte_numero(856)
    print(inverte)

# EU
def inverte(num):
    if num < 10:
        return num
    return (str(num))[::-1]

inv = inverte(856)
print(inv)