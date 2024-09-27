from math import hypot
ad = float(input('\033[1;31m comprimento do cateto adjacente: '))
op = float(input('\033[1;31m comprimento do cateto oposto: '))
ss = hypot(ad, op)
print('\033[1;31m a hipotenusa é {:.2f}\033[m'.format(ss))