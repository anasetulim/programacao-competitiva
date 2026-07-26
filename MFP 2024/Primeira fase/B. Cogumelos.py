import math

p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))
p4 = list(map(int, input().split()))

area = (min(math.dist(p1,p2), math.dist(p1,p3), math.dist(p1,p4)))**2

print(int(area))