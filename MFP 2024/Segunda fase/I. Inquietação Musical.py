n = int(input())
versos = []
for i in range(n):
    verso = map(str, input().split())
    versos.append(verso)

m = int(input())
notas = {}
for i in range(m):
    p, x = input().split()
    notas[p] = int(x)

soma_trecho = 0
maior_nota_verso = -1
melhor_indice = -1

for indice, verso in enumerate(versos, 1):
    soma_verso = 0

    for palavra in verso:
        if palavra in notas:
            soma_verso += notas[palavra]          
    soma_trecho += soma_verso
    
    if soma_verso >= maior_nota_verso:
        maior_nota_verso = soma_verso
        melhor_indice = indice

print(f'{soma_trecho} {melhor_indice}')