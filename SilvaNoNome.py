#Faça um programa que leia um nome de uma pessoa é diga se ela possui "SILVA" no nome.
n = str(input('Digite o seu nome: ')).upper().strip()
print('O nome {}, possui SILVA {}'.format(n, 'SILVA' in n))
