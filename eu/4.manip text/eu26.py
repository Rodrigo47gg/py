frase = str(input('\033[1;32mdigite uma frase: ')).upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count("A")))
print('a primeira letra A apareceu na posição {}'.format(frase.find("A")+1))
print('a ultima letra A apareceu na posição {}\033[m'.format(frase.rfind("A")+1))