n = int(input())

ponto_t1 = 0
ponto_t2 = 0

for i in range(n):
    l = input()
    t = int(l[5])
    k = int(l[8])

    if t==1:
        ponto_t1 += k
    else:
        ponto_t2 += k

print(f'{ponto_t1} x {ponto_t2}')