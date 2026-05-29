#D
from functools import reduce
import math

n = int(input())
a = list(map(int, input().split()))
mdc = reduce(math.gcd, a)
resultado = sum(a)//mdc
print(resultado)