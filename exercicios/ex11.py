lg = float(input('qual a largura da sua parede: '))
at = float(input('qual a altura da sua parede: '))
print('sua parede tem a dimensao de {}*{} e sua area é de {}²'.format(lg, at, lg*at))
print("para pintar essa parede, você precisa de {}L de tinta".format((lg*at)/2))