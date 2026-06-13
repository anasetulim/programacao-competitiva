import bisect #serve para fazer busca binária em listas ordenadas
 
n, m = map(int, input().split())
lista_n = list(map(int, input().split()))
lista_m = list(map(int, input().split()))
 
lista_n.sort() #a lista precisa estar ordenada
lista_final = []
 
#para cada elemento da lista m, encontrar quantos na lista n são <= ele
for valor in lista_m:
    qtd = bisect.bisect_right(lista_n, valor) 
    lista_final.append(qtd)
 
#imprimi tudo na mesma linha, sem ser em formato de lista
print(*lista_final)