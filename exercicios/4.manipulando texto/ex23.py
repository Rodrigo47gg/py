num = int(input('digite um numero: '))
un = num // 1 % 10
de = num // 10 % 10
cem = num // 100 % 10
mil = num // 1000 % 10
print('analizando o numero: {}'.format(num)) 
print('unidade:{}'.format(un))
print('dezena:{}'.format(de))
print('centena:{}'.format(cem))
print('milhar:{}'.format(mil))