n = int(input())
p = int(input())
k = int(input())

roda = list(range(1,n+1))
roda.remove(p)

sentadas = n-1 #criança p levantou
indice_ganso = (p-1+k)%sentadas #p-1 é o índice atual da criança seguinte a que levantou

print(roda[indice_ganso])

