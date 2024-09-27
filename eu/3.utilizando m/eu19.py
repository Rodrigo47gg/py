#sortea aluno
import random
al1 = str(input('\033[1;31m primeiro aluno: \033[m'))
al2 = str(input('\033[1;31m segundo aluno: \033[m'))
al3 = str(input('\033[1;31m terçeiro aluno:\033[m'))
al4 = str(input('\033[1;31mquarto aluno:\033[m'))
lista = [al1, al2, al3, al4]
tr = random.choice(lista)
print('\033[1;31m o aluno escolhido é o {}'.format(tr))