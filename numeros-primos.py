cont = 0
n = int(input('Digite um numero para saber se o mesmo e primo: '))
for i in range(1, n + 1):
  if n % i == 0:
    print('\033[34m', end='')
    cont+=1
  else:
    print('\033[31m', end='')
  print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele Não é PRIMO')
