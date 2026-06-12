n = int(input())

instrucoes = []
for i in range(n):
    instrucao = input()
    instrucoes.append(instrucao)

x = 0
for instrucao in instrucoes:
    if "++" in instrucao:
        x += 1
    else:
        x -= 1

print(x)