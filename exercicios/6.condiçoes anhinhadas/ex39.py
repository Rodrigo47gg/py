from datetime import date
atual = date.today().year
ano = int(input('ano de nascimento: '))
idade = atual - ano
if idade == 18:
    print('quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    print('você deve se alistar imediatamente!')
elif idade < 18:
    print('quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    falta = 18 - idade
    print('ainda faltam {} anos para o alistamento'.format(falta))
    ss = atual + falta
    print('seu alistamento será em {} anos'.format(ss))
elif idade > 18:
    print('quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
    passou =  idade - 18
    print('voce já deveria ter se alistado há {} anos'.format(passou))
    fim = atual - passou
    print('seu alistamento foi em {}'.format(fim))