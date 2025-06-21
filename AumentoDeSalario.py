#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento :)
from time import sleep
print('{:=^40}'.format('Aumento Salárial'))
s = int(input('Digite aqui seu salário atual: '))
print('Calculando seu aumento...')
sleep(3)
print('Seu novo salário aplicando aumento de 15%: {:.1f}R$'.format(s+(s*15/100)))
print('Seu aumento consiste no valor de: {}R$'.format(s*15/100))