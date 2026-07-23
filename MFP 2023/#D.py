m1, m2 = map(float, input().split())
x1, x2 = map(float, input().split()) 
f = float(input())

d = abs(x1 - x2)

g = (f*(d**2))/(m1*m2)

print(f'{g:.6f}')