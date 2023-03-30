#Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N. Por exemplo, o dígito 2 ocorre 3 vezes em 762021192. 

def count_digit(n, k):
    if n == 0:
        return 0
    elif n % 10 == k:
        return 1 + count_digit(n // 10, k)
    else:
        return count_digit(n // 10, k)
    
n = 762021192
k = 2
print(f"O digito {k} ocorre {count_digit(n, k)} vezes em {n}")  

