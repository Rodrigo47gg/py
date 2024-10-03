from datetime import date
atual = date.today().year
print("\033[1;31m===\033[m" * 25)
masc = print('\033[1;31m[1] MASCULINO\033[m')
femi = print('\033[1;32m[2] FEMININO\033[m')
escolha = int(input('\033[1;33mQUAL O SEU SEXO: \033[m'))
print('\033[1;31m===\033[m' * 25)
if escolha == 1:
    print('===============HOMEN===============')
    print('\033[1;31m===ALISTAMENTO OBRIGATORIO===\033[m')
    ano = int(input('\033[2;33mANO DE NASCIMENTO: \033[m'))
    idade = atual - ano
    #tem 18 anos
    if idade == 18:
        print('\033[1;34m==================URGENTE==================\033[m')
        print(f'\033[1;34mquem nasceu em {ano} tem {idade} anos em {atual}\033[m')
        print('\033[1;34mvocê deve se alista imediatamente!\033[m')
    #menos de 18
    elif idade < 18: 
        print(f'\033[1;36mquem nasceu em {ano} tem {idade} anos em {atual}\033[m')
        falta = 18 - idade
        print(f'\033[1;36mainda faltam {falta} anos para o alistamento\033[m')
        futuro = atual + falta
        print('\033[1;36mseu alistamento será em {}\033[m'.format(futuro))
    #mais de 18
    elif idade > 18:
        print(f'quem nasceu em {ano} tem {idade} anos em {atual}')
        passou = idade - 18
        print(f"você deveria ter se alistado a {passou} anos")
        anodoalis = atual - passou
        print(f'voce deveria ter se alistado em {anodoalis}')
    #singular
    elif idade == 17:
        print(f'quem nasceu em {ano} tem {idade} anos em {atual}')
        faa = 18 - idade
        print(f'ainda falta {faa} ano')
        fut = atual + faa
        print(f'seu alistamento sera em {fut}')
        #sexo feminino
elif escolha == 2:
    print('alistamento opsional')