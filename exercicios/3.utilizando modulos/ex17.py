"""ct = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (ct ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa é {:.2f}'.format(hi))"""
import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))