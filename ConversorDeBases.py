#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolha qual será a base de convenção: 1 - para Binário, 2 - Octal, 3 - Hexadecimal
print('{:=^40}'.format('Conversor de Bases Númericas'))
n = int(input('Digite um número inteiro que seja converter: '))
print('Escolha uma base númerica para conversão. 1 - Binário, 2 - Octal, 3 - Hexadecimal')
b = int(input('Digite qual Base de Conversão [1,2,3]: '))
if b == 1:
    print('O {} número convertido para binário é igual a {}'.format(n, bin(n) [2:]))
elif b == 2:
    print('O {} número convertido para Octal é igual a {}'.format(n, oct(n) [2:]))
elif b == 3: 
    print('O {} convertido para Hexadecimal é igual a {}'.format(n, hex(n) [2:]))
else:
    print('OPÇÃO INVALIDA')