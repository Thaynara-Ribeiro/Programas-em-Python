#Faça um programa que leia o nome completo de uma pessoa, informando o primeiro/ultimo nome separadamente.
print('{:=^40}'.format('Analisando um Nome'))
n = str(input('Informe o seu nome: ')).strip().upper().split()
print('Primeiro Nome: {}'.format(n[0]))
print('Ultimo Nome: {}'.format(n[len(n)-1]))