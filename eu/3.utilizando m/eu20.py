al1 = str(input('\033[1;31m primeiro aluno: \033[m'))
al2 = str(input('\033[1;32m segundo aluno: \033[m'))
al3 = str(input('\033[1;33m terceiro aluno: \033[m'))
al4 = str(input('\033[1;34m quarto aluno: \033[m'))
lista = [al1, al2, al3, al4]
import random
ss = random.shuffle(lista)
print("\033[1;31m {}\033[m".format(lista))