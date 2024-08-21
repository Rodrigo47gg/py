import random
n1 = input('nome do primeiro aluno: ')
n2 = input('nome do segundo aluno: ')
n3 = input('nome do terceiro aluno: ')
n4 = input('nome do quarto aluno: ')
listas = [n1, n2, n3, n4]
random.shuffle(listas)
print('a ordem de apresentaçao é')
print(listas)