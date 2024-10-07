a1 = float(input('qual o comprimentodo do primeiro angulo: '))
a2 = float(input('qual o comprimento do segundo angulo: '))
a3 = float(input('qual o comprimento do terçeiro angulo: '))
if a1 < a2 + a3 and a1 < a2 + a3 and a1 < a2 + a3:
    print('forma um triangulo')
    if a1 == a2 == a3 and a2 == a1 == a3 and a3 == a1 == a2:
        print('os seguimentos acima podem forma um triangulo equilatero')
    elif a1 == a2 != a3 and a2 == a1 != a3 and a3 == a1 != a2:
        print('os seguimentos acima podem forma um triangulo isoscelis')
    elif a1 != a2 != a3 and a2 != a1 != a3 and a3 != a1 != a2:
        print('os seguimentos acima podem formar um triangulo escaleno')
else:
    print('não forma um triangulo')