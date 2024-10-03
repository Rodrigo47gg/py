ano = int(input('qual a sua idade: '))
ss = 2024 - ano
if ss < 9:
    print(f'sua idade e {ss}')
    print('mirim')
elif ss > 10 and ss < 18:
    print(f'sua idade é {ss}')
    print('infantil')
elif ss == 19:
    print(f'sua idade é {ss}')
    print('junior')
elif ss == 20:
    print(f'sua idade é {ss}')
    print('senior')
elif ss > 20:
    print(f'sua idade é {ss}')
    print('master')