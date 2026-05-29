#F
n, k = map(int, input().split())
l = list(map(int, input().split()))
prob = 1

for i in l:
    if i < k:
        prob *= 1
    else:
        prob *= (k-1)/i

resultado = 1-prob
print(resultado)