dia = int(input('quantos dias voce alugol o carro: '))
km = float(input('quantos km voce dirigil: '))
print('voce alugol o carro por {} dias\n andou {}KM \n isso vai custar R$:{}'.format(dia, km,((dia * 60) + (km * 0.15))))