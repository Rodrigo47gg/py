#indice de massa corporal
peso = float(input('qual o seu peso:(kg)'))
alt = float(input('qual a sua altura'))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('você esta ABAIXO do peso')
    elif 