sala = float(input("qual é o salario do funcionario? R$:"))
raj = (sala * 15)/100
print('um funcionario que ganhava R$:{}, com 15% de aumento passa a receber R$:{:.2f}'.format(sala, (sala + raj)))