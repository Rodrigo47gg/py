"""sorteio de aluno"""
import random
al1 = input('nome do aluno: ')
al2 = input('nome do aluno: ')
al3 = input('nome do aluno: ')
al4 = input('nome do aluno: ')
lista = [al1, al2, al3, al4]
ss = random.choice(lista)
print('escolhemos o {}'.format(ss))