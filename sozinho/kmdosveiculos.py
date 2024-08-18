di = float(input('quantos dias usei o carro: '))
km = float(input('quantos km andei com o carro: '))
sbt = km * 0.15 + di * 60
print('você tera que pagar R$:{}'.format(sbt))
a1 = int(input('em quantas parcelas você pretende pagar: '))
print('6%, de acrecimo')
sd = (sbt * 6)/100
al = sbt + sd
print('você vai pagr {} vezez de R$:{}'.format(a1, al/a1))
