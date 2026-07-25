t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    for dono_original in range(1, n + 1): #bicicleta de cada amigo
        caminho = [dono_original]
        atual = dono_original
        
        while True:
            proximo = p[atual - 1]  

            if proximo == dono_original:
                break
            
            caminho.append(proximo) 
            atual = proximo
            
        print(*caminho) #* desempacota a lista