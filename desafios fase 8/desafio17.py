'''cateto e ipotenuza'''
co = float(input('quanto mede o cateto oposto:'))
cat = float(input('qual o comprimento do cateto adjacente:'))
hi = (co ** 2 + cat ** 2) ** (1/2)
print('a hipotenuza vai medir {:.2f}'.format(hi))