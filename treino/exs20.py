import random
al1 = input('primeiro aluno: ')
al2 = input('segundo aluno: ')
al3 = input('terceiro aluno: ')
al4 = input('quarto aluno: ')
pas = [al1, al2, al3, al4]
random.shuffle(pas)
print(pas)