#reajuste salarial..
sla = float(input('\033[1;31m qual é o salario do funcionario: \033[m'))
ss = (sla * 15)/100
print('\033[1;33mum funcionario que ganhava R$:{}, com 15% de aumento, passa a receber R$:{:.2f}.\033[m'.format(sla, sla + ss))