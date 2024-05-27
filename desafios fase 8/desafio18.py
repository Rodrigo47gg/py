from math import radians, sin, cos, tan
am = float(input('digite o angulo que voce deseja'))
seno = sin(radians(am))
print('o angulo {} tem o seno {:.2f}'.format(am, seno))
co = cos(radians(am))
print('o angulo de {} tem o cosseno de {:.2f}'.format(am, co))
tg =tan(radians(am))
print('o angulo de  {} tem a tangente de {:.2f}'.format(am, tg))