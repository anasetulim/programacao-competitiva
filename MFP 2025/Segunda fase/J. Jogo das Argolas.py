p_rosa, p_azul = map(int, input().split())
a = int(input())

#a pontuação máxima é dada qnd x e y são o mais próximo possível
x = a//2
y = a - x
p_max = (x*p_rosa)*(y*p_azul)

print(p_max)


