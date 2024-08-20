sl = float(input('qual é o salario do funcionario: '))
se = (sl*15)/100
df = sl + se
print('um funcionario que ganhava {}, com 15%, de aumento, passara a receber {:.2f}'.format(sl, df))