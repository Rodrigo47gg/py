#0.50 ate 200km e 0.45 para mais de 200km
kms = float(input('\033[1;31mqual a distâcia da sua viagem: '))
if kms >= 200:
    ss = kms * 0.45
    print('você esta prestes a começar uma viagem de {}'.format(kms))
    print('e o preço da sua pasagem e de {}'.format(ss))
else:
    ff = kms * 0.50
    print('voce esta prestes a começar uma viagem de {}'.format(kms))
    print('e o preço da sua passagem e de {}\033[m'.format(ff))