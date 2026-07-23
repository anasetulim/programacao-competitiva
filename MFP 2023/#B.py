n = int(input())
h = list(map(int, input().split()))
maior_planta = 0

h.sort()

for i in range(n):
    altura_planta = ((h[i]) + h[n-1-i])/2 #compensando a altura fazendo a média entre a menor e a maior planta
    if altura_planta > maior_planta:
        maior_planta = altura_planta

print(maior_planta)