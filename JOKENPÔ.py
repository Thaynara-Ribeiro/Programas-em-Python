#Faça o computador jogar JOKENPÔ com você (Pedra, Papel, Tesoura)
from random import randint
from time import sleep
itens = ['PEDRA' , 'PAPEL' , 'TESOURA']
computador = randint(0 ,2)
print('''Escolha uma opção abaixo para Jogar JOKENPÔ: 
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual sua opção? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
if computador == 0: # Computador escolhe PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2: 
        print('COMPUTADOR VENCE')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 1: # Computador escolhe PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2: 
        print('JOGADOR VENCE')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 2: # Computador escolhe TESOURA 
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2: 
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA')