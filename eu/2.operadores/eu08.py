med = int(input('\033[1;30;47m uma distacia em metros: \033[m'))
dm = med*10
cm = med*100
mm = med*1000
dam = med/10
hm = med/100
km = med/1000
print("\033[1;31;46m{} e igual a {}kilometros\033[m".format(med, km))
print("\033[1;32;45m{} e igual a {}hectômetros\033[m".format(med, hm))
print("\033[1;33;44m{} e igual a {}dametros\033[m".format(med, dam))
print("\033[1;34;43m{} e igual a {}decametros\033[m".format(med, dm))
print("\033[1;35;42m{} e igual a {}centimetros\033[m".format(med, cm))
print("\033[1;36;41m{} e igual a {}milimetros\033[m".format(med, mm))