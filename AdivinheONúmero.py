#Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 até 5 para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deve retornar se o usuário ganhou ou perdeu o jogo.
from random import randint

print('{:=^40}'.format('Adivinhe o Número'))
computador = randint(0, 5)
chute = int(input('Usuário adivinhe qual número estou pensando de 0 até 5: '))
if chute == computador:
    print('PARABENS, você acertou eu pensei exatamente {}'.format(computador))
else:
    print('NÃO FOI DESSA VEZ, o número pensado foi {}'.format(computador))
while chute != computador:
    computador = randint(0, 5)
    chute = int(input('Usuário adivinhe qual número estou pensando de 0 até 5: '))
    if chute == computador:
        print('PARABENS, você acertou eu pensei exatamente {}'.format(computador))
    else:
        print('NÃO FOI DESSA VEZ, o número pensado foi {}'.format(computador))

