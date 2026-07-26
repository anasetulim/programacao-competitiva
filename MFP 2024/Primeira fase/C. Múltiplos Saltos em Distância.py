n = int(input())
a = list(map(int, input().split()))

moedas = a[:]

for i in range(len(a) - 1, -1, -1): #percorrendo a árvore de trás p frente
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < len(a):
        moedas[i] += max(moedas[esquerda], moedas[direita]) #escolhendo o caminho q da +moedas

print(moedas[0])