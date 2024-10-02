'''
***Problema***
Crie um programa que gere um número aleatório de 0 até 10.
E que o usuário possa realizar chutes, retornando se o chute do mesmo foi "Maior que o número gerado"
"Menor que o número gerado" ou "Acertou o Chute" O programa deve perguntar ao usúario se o mesmo deseja continuar
jogando até se encerrar com o mesmo acertando o chute ou negando a continuação
Utilizando o Metodo 5Qs
Qual os dados de entrada?
Oque fazer com esses dados?
Qual as restrições do programa?
Qual o resultado esperado?
Qual a sequência de passo a passo em Pseudocódigo?
'''
'''Solução'''
from random import randint
controle = 'S'
while controle == 'S':
    print('======= Jogo de Adevinhação =======')
    acertou = 'S'
    robot = randint(0,10)
    while acertou == 'S':
        chute = int(input('Qual o seu chute? [0 até 10]: '))
        if chute > robot:
            print('Chute MAIOR que número gerado')
        elif chute < robot:
            print('Chute MENOR que número gerado')
        else:
            print('ACERTOUUU')
            print('O numero gerado foi exatamento {}'.format(robot))
            acertou = 'n'
    controle = input('Deseja continuar? [S/N] ')
    
