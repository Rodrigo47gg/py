import math
gr = float(input('digite o angulo que você deseja: '))
co = math.cos(math.radians(gr))
ta = math.tan(math.radians(gr))
se = math.sin(math.radians(gr))
print('o coseno de {} é {:.2f}'.format(gr, co))
print('a tangente de {} é {:.2f}'.format(gr, ta))  
print('o seno de {} é {:.2f}'.format(gr, se))