'''tinta na parede'''
larg = float(input('largura da parede:'))
alt = float(input('altura da parede:'))
area = larg * alt
print('sua parede tem a dimensao de {}*{} e sua area e de {}metros'.format(larg, alt, area))
tinta = area / 2
print('para pintar essa parede você precisará de {} litros de tinta'.format(tinta))