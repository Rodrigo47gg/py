import random
num = int(input('\033[1;31m adivinhe o numero: '))
ss = random.randint(0, 5)
if num == ss:
    print('PARABENS, você acertou!')
else:
    print("INFELIZMENTE você errou!")
print('==FIM==\033[m')