from random import randint
count = 0
print('{:=^40}'.format(' Vou pensar em um numero de 0 á 10, tente adivinhar. '))
jogo = int(input('Em qual numero pensei? '))
escolha = randint(0, 10)
while escolha != jogo:
  print('Continue tentando')
  count+=1
  jogo = int(input('Em qual numero pensei? '))
if jogo == escolha:
    print('Você acertou a resposta é {}, mas para isso foi necessário {} tentativas'.format(escolha ,count))
