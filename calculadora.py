from time import sleep
print('==== Desafio 01 ===')
print('''CALCULADORA
Escolha as seguintes opções:
1 - Para Somar
2 - Para Subtrair
3 - Para Multiplicar
4 - Para Dividir
''')
escolha = int(input('Qual operação você deseja realizar? '))
if escolha != 1 or 2 or 3 or 4:
    print('OPÇÃO INVALIDA')
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
sleep(1)
print('Calculando...')
sleep(1)
if escolha == 1:
    print('A soma desses dois valores é igual= {}'.format(num1+num2))
elif escolha ==2:
    print('A subtração desses dois valores é igual= {}'.format(num1-num2))
elif escolha ==3:
    print('A multiplicação desses dois valores é igual= {}'.format(num1*num2))
elif escolha ==4:
    print('A divisão desses dois valores é igual= {}'.format(num1/num2))
else:
    print('OPÇÃO INVALIDA')






