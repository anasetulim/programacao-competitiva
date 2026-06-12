n = int(input())
palavra = input().lower()

#a = set("abc")
#b = set("abcdef")
#print(a.issubset(b))  # True
#'tudo que está em a está em b?'

if set("abcdefghijklmnopqrstuvwxyz").issubset(set(palavra)):
    print('SIM')
else:
    print('NÃO')