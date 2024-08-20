co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
ss = (co ** 2) + (ca ** 2)
from math import sqrt
pa = sqrt(ss)
print('a hipotenusa vai medir {:.2f}'.format(pa))