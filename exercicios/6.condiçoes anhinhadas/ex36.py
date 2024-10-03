cs = float(input('qual o valor da casa R$: '))
sla = float(input('salario do comprador R$: '))
fnc = int(input('quantos anos de finaciamento: '))
ss = cs / (fnc * 12)
porc = (sla * 30)/100
print('para pagar uma casa de {} em {} anos a prestação será de R$:{:.2f}'.format(cs, fnc, ss))
if ss <= porc:
    print('emprestimo pode ser concedido')
else:
    print('emprestimo recusado')