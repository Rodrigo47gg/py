import random
alu1 = input('nome do primeiro aluno: ')
alu2 = input('nome do segundo aluno: ')
alu3 = input('nome do terçeiro aluno: ')
alu4 = input('nome do quato aluno: ')
lista =  [alu1, alu2, alu3, alu4]
escolhido = random.choice(lista)
print('o aluno escolhido foi o {}'.format(escolhido))
#choice faz parte do random