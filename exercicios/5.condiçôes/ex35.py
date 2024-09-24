n1 = float(input('primeiro seguimento: '))
n2 = float(input("segundo seguimento: "))
n3 = float(input('terçeiro segimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('os segmentos a cima PODEM FORMA TRISNGULO')
else:
    print('os segmentos a cima NAO PODEM FORMA TRIANGULO')