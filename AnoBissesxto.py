#Faça um programa que leia se um ano qualquer é ou não Bissexto.
a = int(input('Digite um Ano qualquer: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O Ano {} é Bissexto'.format(a))
else:
    print('O Ano {} não é Bissexto'.format(a))