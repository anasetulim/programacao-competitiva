t = int(input())

for i in range(t):
    k1, k2, k3 = list(map(int, input().split()))

if k1 != k2 and k1 != k3:
    print(k1)
elif k2 != k1 and k2 != k3:
    print(k2)
else:
    print(k3)
