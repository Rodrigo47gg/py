#60 por dia 
#0.15 por km rodado
dia = int(input("\033[1;31mquantos dias alugados: \033[m"))
km = int(input('\033[1;31m quantos km rodados: \033[m'))
ss = dia * 60
jj = km * 0.15
res = ss + jj
print('\033[1;31m o total a pagar é de R$:{}\033[m'.format(res))