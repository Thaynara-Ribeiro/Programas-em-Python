#Faça um programa que leia o nome completo de uma pessoa, ao receber nome mostre em tela o nome todo maiusculo, minusculo, qunatidade de caracters sem espaços e a quantidade de letras no primeiro nome.
print('{:=^40}'.format('Manipulando uma String'))
n = str(input('Digite o seu nome completo: ')).strip()
print('Nome Maiusculo: {}'.format(n.upper()))
print('Nome Minusculo: {}'.format(n.lower()))
print('O nome possui {} espaços na memória'.format(len(n)))
s = n.split()
print('O primeiro nome {} possuindo {} letras'.format(s[0], len(s[0])))