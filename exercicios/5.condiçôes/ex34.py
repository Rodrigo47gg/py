sla = float(input('qual o salario do funcionario:').strip())
if sla >= 1250:
    ma = (sla * 10)/100
    tt = ma + sla
    print("seu salario de {} passa a ser {}".format(sla,tt))
else:
    me = (sla * 15)/100
    ts = me + sla
    print('seu salario de {} passa a ser {}'.format(sla,ts))