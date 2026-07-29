import math

a, b = map(int, input().split())
for i in range(1, 100000):
    if a%i==0 and a-b<=i:
        resposta = i
        break

print(resposta)
    