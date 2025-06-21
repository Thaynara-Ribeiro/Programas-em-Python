#Faça um programa que ao receber o valor dá carteira do usuario, calcule o valor convertendo para Dolar
#Use Cotação Atual
print('{:=^40}'.format('Conversor de Moedas'))
n = int(input('Digite o Valor em R$: '))
print('Seu valor convertido em Dolares é {:.2f}$'.format(n/6.09))