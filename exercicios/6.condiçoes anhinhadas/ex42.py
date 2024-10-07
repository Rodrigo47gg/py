a1 = float(input('qual o comprimentodo do primeiro angulo: '))
a2 = float(input('qual o comprimento do segundo angulo: '))
a3 = float(input('qual o comprimento do terçeiro angulo: '))
if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print("os segmentos acima PODEM FORMAR um triangulo", end=" ")
    if a1 == a2 == a3:
        print("EQUILATERO!")
    elif a1 != a2 != a3 != a1:
        print('escaleno!')
    else:
        print('isosceles')
else:
    print('os seguimentos acima NÃO PODEM forma um triangulo')