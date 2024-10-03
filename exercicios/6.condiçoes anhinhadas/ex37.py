num = int(input('digite um numero inteiro: '))
print('escolha uma das bases para conversão')
print('\033[1;31m[1] converte para binário\033[m')
print("\033[1;32m[2] converte para octal\033[m")
print("\033[1;33m[3] converte para hexadecimal\033[m")
op = int(input('escola uma das opçoes: '))
if op == 1:
    print('{} convertido para binario é igual a {}'.format(num ,bin(num).replace('0b','')))
elif op == 2:
    print('{} convertendo para octal é igual a {}'.format(num, oct(num).replace("0o",'')))
elif op == 3:
    print('{} convertendo para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida!')