#Crie um progranma que leia um número inteiro qualquer em tela informando se o mesmo é PAR ou IMPAR
print('{:=^40}'.format('PAR ou IMPAR'))
n = int(input('Digite um número qualquer: '))
if n % 2 == 0:
    print('Número PAR')
else: 
    print('Número IMPAR')