n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, o produto é {} e a divisao é {:.3f}'.format(s, m, d), end=' ')
print(' a divisao inteira é {} e a potencia {}'.format(di, e))