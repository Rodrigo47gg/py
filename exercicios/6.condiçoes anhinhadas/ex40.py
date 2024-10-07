n1 = float(input("primeira nota: "))
n2 = float(input('segunda nota: '))
media = (n1 + n2) / 2
print('sua media foi é {}'.format(media))
if media <=5:
        print('você foi reprovado!')
elif media >= 5 and media < 6.9:
        print('vecê esta de recuperação!')
elif media > 7:
        print('você foi aprovado!')