lg = float(input('largura da parede: '))
at = float(input('altura da parede: '))
ss = lg * at
gg = ss / 2
print('sua parede tem a dimensão {}*{} e sua area é de {}²'.format(lg, at, ss))
print('para pintar essa parede, você precisara de {}l de tinta'.format(gg))