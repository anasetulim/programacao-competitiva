#C
L, C = map(int, input().split())
n = (L//7) * (C//1)   
m = (L//1) * (C//7)

print(max(n, m))