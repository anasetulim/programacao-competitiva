n, m = map(int, input().split())
a = list(map(int, input().split()))

frequencia = [0]*(m+1)

for i in a:
    if i <= m:
        frequencia[i] += 1
    else:
        frequencia[m] += 1

resposta = [0]*(m+1)
resposta[m] = frequencia[m]

for i in range(m-1, 0, -1):
    resposta[i] = frequencia[i] + resposta[i+1]

print(*resposta[1:])