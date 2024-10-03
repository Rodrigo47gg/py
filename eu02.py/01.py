import random
print('\033[1;31m ===\033[m'*20)
res = int(input('[1]PEDRA\n[2]PAPEL\n[3]TESOURA\nescolha uma opção: '))
print('\033[1;31m ===\033[m' * 20)
lista = ['pedra', 'papel', 'tesoura']
ss = random.choice(lista)
if res == 1 and ss == 'pedra' or res == 2 and ss == 'papel' or res == 3 and ss == 'tesoura':
    print('empatou, tente novamente')
elif res == 1 and ss == 'tesoura' or res == 2 and ss == 'pedra' or res == 3 and ss == 'papel':
    print('parabens, você ganhou!')
elif ss == 'pedra' and res == 3 or ss == 'papel' and res == 1 or ss == 'tesoura' and res == 2:
    print('infelizmente você perdeu!')
else:
    print('nenhuma opção escolhida!')