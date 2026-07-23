i1, i2, i3, i4, i5, i6, i7, i8 = map(int, input().split())

soma = i1 + i2 + i3 + i4 + i5 + i6 + i7

if i8 == 0 and soma%2 == 0:
    print("N?")
elif i8 == 1 and soma%2 == 1:
    print("N?")
else:
    print("S")
