import math
an = int(input('digite o angulo que você deseja: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print('o ângulo de {} tem o seno de {:.2f}'.format(an, se))
print('o ângulo de {} tem o cosseno de {:.2f}'.format(an, co))
print('o ângulo de {} tem a tangente de {:.2f}'.format(an, ta))