n1 = int(input("digite o primeiro valor: "))
n2 = int(input('digite o segundo valor: '))
n3 = int(input('digite o terçeiro valor: '))
me = n1
if n2<n1 and n2<n3:
    me = n2
if n3<n2 and n3<n2:
    me = n3
mai = n1
if n2>n1 and n2>n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3
print('o menor valor foi {}'.format(me))
print('o maior valor foi {}'.format(ma))