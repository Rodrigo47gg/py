gr = float(input('\033[1;31m informe a temperaturs em ºC: \033[m'))
ss = gr * 1.8
print('\033[1;31m a temperatura de {} corresponde a {:.1f}°F!\033[m'.format(gr, ss + 32))