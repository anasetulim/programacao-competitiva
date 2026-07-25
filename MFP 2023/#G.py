n, m = map(int, input().split())

for i in range(m):
    l, r = map(int, input().split())

#a sequencia ótima é a de flores alternadas
sequencia = ('01'*n)[0:n]

print(sequencia)