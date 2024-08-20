dia = int(input('quantos dias alugados: '))
kms = int(input('quantos kms rodados: '))
ss = dia * 60
sw = kms * 0.15
al = ss + sw
print('o total a pagar é de {:.2f}'.format(al))