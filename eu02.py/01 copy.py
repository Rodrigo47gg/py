import random
print('\033[1;31m ===\033[m'*20)
res = int(input('[1]STONE\n[2]PAPER\n[3]SCISSORS\nchoose an option: '))
print('\033[1;31m ===\033[m' * 20)
lista = ['rock', 'paper', 'scissors']
ss = random.choice(lista)
if res == 1 and ss == 'rock' or res == 2 and ss == 'paper' or res == 3 and ss == 'scissors':
    print('draw, try again')
elif res == 1 and ss == 'scissors' or res == 2 and ss ==  'rock' or res == 3 and ss == 'paper':
    print('congratulations, you won!')
elif ss ==  'rock' and res == 3 or ss == 'paper' and res == 1 or ss == 'scissors' and res == 2:
    print('unfortunately you lost!')
else:
    print('no option chosen!')