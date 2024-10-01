num = int(input('\033[1;31mme diga um numero qualquer: '))
ss = num  % 2
if ss == 0:
    print('o numero {} e par'.format(num))
else:
    print('o numero {} e impar\033[m'.format(num))