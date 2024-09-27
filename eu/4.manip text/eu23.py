num = int(input('\033[1;36minforme um numero: \033[m'))
Un1 = num // 1 % 10
d1 = num // 10 % 10
c1 = num // 100 % 10
m1 = num // 1000 % 10
print('\033[1;31manalizando o numero {}'.format(num))
print('unidade {}'.format(Un1))
print('dezena {}'.format(d1))
print('centena {}'.format(c1))
print('dezena {}\033[m'.format(m1))