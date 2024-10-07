#indice de massa corporal
peso = float(input('qual o seu peso:(kg): '))
alt = float(input('qual a sua altura: '))
imc = peso / (alt ** 2)
print('{:.1f}'.format(imc))
if imc < 18.5:
    print('você esta ABAIXO do peso')
elif imc > 18.5 and imc < 25:
    print('você esta no seu IDEAL')
elif imc > 25 and imc < 30:
    print('você esta SOBREPESO')
elif imc > 30 and imc < 40:
    print('você esta com obsedade')
elif imc > 40:
    print('você esta com obsidade morbida')