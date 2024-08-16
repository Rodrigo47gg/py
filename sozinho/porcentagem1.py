valor = float(input('qual o valor do produto R$: '))
ac = int(input('qual o valor do acrecimo:'))
pc = int(input('quantas parcelas:'))
sm = valor + (valor * ac) / 100
pr = sm / pc
print('o produto cuta R$:{} com acrecimo de {}%'.format(sm, ac))
print("em parcelas de {} de {:.2f}".format(pc, pr))