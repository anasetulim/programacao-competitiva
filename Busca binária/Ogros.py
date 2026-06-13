from bisect import bisect_right

n, m = map(int, input().split())
limites = list(map(int, input().split()))
premios = list(map(int, input().split()))
ogros = list(map(int, input().split()))

for força in ogros:
    faixa = bisect_right(limites, força)
    print(premios[faixa], end=' ')