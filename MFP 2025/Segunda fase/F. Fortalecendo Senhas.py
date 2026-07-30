n = int(input())

for i in range(n):
    senha = input()

    if len(senha) <= 10:
        print('N')
        continue

    tem_letra = False
    tem_digito = False
    senha_valida = True

    for i in range(len(senha)):
        if senha[i].isalpha():
            tem_letra = True
        elif senha[i].isdigit():
            tem_digito = True

        if i > 0:
            #se o caractere atual for menor (tabela ASCII) que o anterior, a senha é inválida
            if senha[i] < senha[i-1]:
                senha_valida = False

    if senha_valida and tem_letra and tem_digito:
        print('S')
    else:
        print('N')