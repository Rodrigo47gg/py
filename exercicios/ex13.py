sl = float(input('qual o salario do fumcionario R$:'))
sm = (sl * 15)/100
print('um funcionario que ganhava R${}, com almento de 15%, passa a receber R$:{:.2f}'.format(sl, (sl + sm)))