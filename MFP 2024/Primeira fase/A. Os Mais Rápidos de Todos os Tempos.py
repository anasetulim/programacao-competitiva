n, p = map(int, input().split())
a = list(map(int, input().split()))

tempo_min = 1
tempo_max = min(a)*p #o mais rápido entregando td sozinho
resposta = tempo_max

while tempo_min <= tempo_max:
    meio = (tempo_min+tempo_max)//2
    pizzas = 0

    for i in a:
        pizzas += meio//i

    if pizzas >= p:
        resposta = meio
        tempo_max = meio-1 #se entregaram todas no tempo meio, -1 para achar um tempo menor
    else:
        tempo_min = meio+1 #se não entregaram todas no tempo meio, +1 para achar um tempo maior

print(resposta)