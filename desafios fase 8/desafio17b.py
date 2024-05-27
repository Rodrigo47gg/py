from math import hypot
co = float(input('comprimento do cateto oposto'))
ca = float(input('comprimento do cateto adjacente'))
hi = hypot(co, ca)
print('a hipotenuza vai medir {:.2f}'.format(hi))