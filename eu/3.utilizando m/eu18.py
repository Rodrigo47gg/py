import math
num = float(input('\033[1;32mdigite o ângulo que você deseja: \033[m'))
sen = math.sin(math.radians(num))
Cos = math.cos(math.radians(num))
tag = math.tan(math.radians(num))
print('\033[1;31mo ângulo de {} tem o seno de {:.2f}\033[m'.format(num, sen))
print('\033[1;31mo ângulo de {} tem o coseno de {:.2f}.\033[m'.format(num, Cos))
print('\033[1;31mo ângulo de {} tem a tangente de {:.2f}.\033[m'.format(num, tag))