nt1 = float(input('\033[1;30;40m primeira nota: \033[m'))
nt2 = float(input('\033[1;31;41m segunda nota: \033[m'))
ss = (nt1 + nt2)/2
print('\033[1;32;42m a media da nota {} e {} é {:.2f}\033[m'.format(nt1, nt2, ss))