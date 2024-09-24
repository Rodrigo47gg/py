import random
from time import sleep
cx = int(input('adivimhe o numero: '))
rs = random.randint(0, 10)
print(rs)
print('analizando...')
sleep(3)
if cx ==rs:
    print('você acertou')
else:
    print("você errou")
print("==FIM==")