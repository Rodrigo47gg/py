#pedra, papel e tesolra
import random
res = str(input('escolha [PEDRA, PAPEL OU TESOURA]: ')).strip()
lista = ['papel', 'tesoura', 'pedra']
ss = random.choice(lista)
if res == 'tesoura' and ss == 'tesoura' or res == 'papel' and ss == 'papel' or res == 'pedra' and ss == 'pedra':
    print('tente outra vez')
#==========================================
elif res == "papel" and ss == 'pedra':
    print('parabéns, você venceu!')
    print('pepel vence pedra')
elif ss == 'papel' and res == 'pedra':
    print('você perdeu')
#==========================================
elif res == 'pedra' and ss == 'tesoura':
    print('parabens, você venceu!')
    print('pedra vence tesoura')
elif ss == 'pedra' and res == 'tesoura':
    print('voce perdeu')
#===========================================
elif res == 'tesoura' and ss == 'papel':
    print('parabens, você venceu!')
    print('tesoura vence papel')
elif ss == 'tesoura' and  res == "papel":
    print('você perdeu')
#===========================================
else:
    print('nenhuma opçao escolhida')