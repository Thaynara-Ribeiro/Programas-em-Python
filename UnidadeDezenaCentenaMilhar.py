#Faça um programa que leia um número de 0 a 9999 é mostre na tela cada um dois digitos separados.
# Unidade/Dezena/Centena/Milhar
print('{:=^40}'.format('Analisando um Número'))
n = str(input('Digite um número qualquer: '))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {} '.format(n[0]))

#Essa resposta só funcionará se o usuario desejar analisar um numero com 4 casas decimais... Se desejar que o programa funcione para qualquer número de 0  até 9999 será necessário o fatiamento do mesmo por intermedio de noções matematicas basicas
#Dessa forma abaixo o codigo vai rodar idependente do número digitado pelo usuário.
'''n = int(input('Digite um número qualquer: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {} '.format(n[0]))
'''
