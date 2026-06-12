A,B = input().split(" ")
A = float(A)
B = float(B)

if (A+B)/2 >= 7:
    print('Aprovado')
elif (A+B)/2 < 7 and (A+B)/2 >= 4:
    print('Recuperacao')
else:
    print('Reprovado')