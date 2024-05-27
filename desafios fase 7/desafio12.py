valor = float(input('digite o valor do produto R$:'))
des = (valor * 5)/ 100
print('o produto q custava R$:{},na promoçao com desconto de 5% vai custar R$:{:.2f}reais'.format(valor,(valor - des)))