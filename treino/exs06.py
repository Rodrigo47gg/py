num = int(input('digite um numero: '))
s1 = num * 2
s2 = num * 3
from math import sqrt
s3 = sqrt(num)
print('o dobro de {} é {}'.format(num, s1))
print('o triplo de {} é {}'.format(num, s2))
print('a raiz quadrada de {} é {:.2f}'.format(num, s3))