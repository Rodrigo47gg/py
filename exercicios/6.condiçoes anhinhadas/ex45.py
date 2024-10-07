from random import randint
print('ESCOLHA UMA DAS OPÇÕES\n[0] PEDRA \n[1]PAPEL \n[2]TESOURA')
player =  int(input('QUAL A SUA ESCOLHA: '))
lista = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
print('o computador escolheu {}'.format(lista[computador]))
print('o jogador escolheu {}'.format(lista[player]))
#0 PEDRA #1 PAPEL 2 TESOURA
if computador == 0:
    if player == 0:
        print('EMPATOU!')
        print('VOCÊ EO COMPUTADOR ESCOLHERAM A MESMA COISA')
    elif player == 1:
        print('VOCÊ GANHOU!')
        print('PAPEL VENCE PEDRA!')
    elif player == 2:
        print('VOCÊ PERDEU!')
        print('PEDRA VENCE TESOURA!')
if computador == 1:
    if player == 0:
        print('VOCE PERDEU!')
        print('PAPEL VENCE PEDRA!')
    elif player == 1:
        print('EMPATOU!')
        print('VOCÊ EO COMPUTADOR ESCOLHERAM A MESMA COISA')
    elif player == 2:
        print('VOCÊ VENCEU!')
        print('PAPEL VENCE PEDRA!')
if computador == 2:
    if player == 0:
        print('VOCÊ VENCEU!')
        print('PEDRA VENCE TESOURA!')
    elif player == 1:
        print('VOCÊ PERDEU!')
        print('TESOURA VENCE PAPEL')
    elif player == 2:
        print('EMPATOU!')
        print('VOCÊ EO COMPUTADOR ESCOLHERAM A MESMA COISA')