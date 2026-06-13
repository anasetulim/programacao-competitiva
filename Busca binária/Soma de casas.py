n = int(input())
valores = [int(input()) for valor in range(n)]
k = int(input())

inicio = 0
fim = n-1

while inicio < fim:
    soma = valores[inicio] + valores[fim]
    if soma == k:
        print(valores[inicio], valores[fim])
        break
    elif soma < k:
        inicio += 1
    else:
        fim -= 1