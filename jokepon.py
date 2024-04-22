from random import randint
from time import sleep
print('{:=^40}'.format(' Vamos jogar um jogo '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0 ,3)
print('''Regras do jogo
Pedra quebra tesoura é e enrolada pelo papel
Papel é cortado pela tesoura
Sabendo disso você escolhe
[1] Pedra
[2] Tesoura
[3] Papel ''')
escolha = int(input('Qual a sua escolha? '))
while (escolha != computador):
    escolha = int(input('Qual a sua escolha? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO')
sleep(1)
print('O computador escolheu {}'.format(itens[computador]))
if escolha == 1 and computador == 1:         
    print('EMPATE')
if escolha == 1 and computador == 2:
    print('Você GANHOU')
if escolha == 1 and computador == 3:
    print('Você perdeu mais sorte na proxima vez')
elif escolha == 2 and computador == 1:         
    print('Você perdeu mais sorte na proxima vez')
elif escolha == 2 and computador == 2:
    print('EMPATE')
elif escolha == 2 and computador == 3:
    print('Você GANHOU')
elif escolha == 3 and computador == 1:         
    print('Você GANHOU')
elif escolha == 3 and computador == 2:
    print('Você perdeu mais sorte na proxima vez')
elif escolha == 3 and computador == 3:
    print('EMPATE')
else: 
    print('OPÇÂO INVALIDA, Tente novamente')