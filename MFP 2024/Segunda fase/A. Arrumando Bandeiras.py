import string
n = int(input())

alfabeto = list(string.ascii_lowercase)
bandeira = 'a' 

for i in range(1,n):
    bandeira = bandeira + alfabeto[i] + bandeira

print(bandeira)
