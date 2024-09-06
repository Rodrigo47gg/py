"""dados"""
nome = input('seu nome completo: ').strip()
ss = nome.split()
print('seu nome em maiusculas é {}'.format(nome.upper()))
print('seu primeiro nome é {}'.format(ss[0]))
print(' seu ultimo nome é {}'.format(ss[len(ss)-1]))
print('seu nome sem espaços é {}'.format(nome.replace(' ', '')))