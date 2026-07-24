d, m = map(int, input().split())

tam_corda = d/((2**0.5)/2) #tam do segmento da corda de um prédio até outro
seg_completo = m//tam_corda 
seg_sobra = m%tam_corda

x = m*((2**0.5)/2)

if d == 0:
    y = 0
elif seg_sobra==0 and seg_completo%2==0:
    y = 0
elif seg_sobra==0 and seg_completo%2==1:
    y = d
elif seg_sobra!=0 and seg_completo%2==0: #qntd par de seg, amy ta subindo no eixo y
    y = seg_sobra * ((2**0.5)/2)
elif seg_sobra!=0 and seg_completo%2==1: #qntd ímpar de seg, amy ta descendo no eixo y
    y = d - (seg_sobra * ((2**0.5)/2))

print(f'{x:.6f} {y:.6f}')

