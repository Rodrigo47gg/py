pr = float(input('qual o preço do produto?'))
ss = (pr * 5)/100
aba = pr - ss
print('o produto que custava {}, na promoçao com desconto de 5% vai custar {:.2f}'.format(pr, aba))