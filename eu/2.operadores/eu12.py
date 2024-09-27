va = float(input("\033[1;31m qual é o preço do produto \033[m"))
ss = (va * 5)/100
print('o produto que custava {} na promoção de 5%. de desconto vai custar R$:{}'.format(va, ss + va))