print('{:=^40}'.format(' Progressão '))
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Qual a razão da PA: '))
decimo = pt + (10-1) * r
for i in range(pt, decimo, r):
  print('{} '.format(i), end='-> ')
print('ACABOU')
