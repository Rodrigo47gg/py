#radar eletronico
vl = int(input('\033[1;32mqual é a velocidade atual do carro: \033[m'))
if vl >= 80:
    ss = vl - 80
    print('\033[1;31m você foi multado em R$:{}\033[m'.format(ss * 7.00))
else:
    print('\033[1;32mtenha em bom dia! dirija com segurança!\033[m')