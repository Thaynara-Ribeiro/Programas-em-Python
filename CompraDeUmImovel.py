#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestaçaõ mensal, sabendo que ela não pode exceder 30% do salário do comprador ou a compra do imovel será NEGADA
print('{:=^40}'.format('Consultando Compra de Imovel'))
c = int(input('Digite o Valor do Imovel Desejado: '))
s = int(input('Digite seu Salário Atual: '))
a = int(input('Em quantos anos você deseja pagar seu imovel? '))
p = c / (a*12)
if p < s*(30/100):
    print('COMPRA APROVADA, suas parcelas ficaram em {}x de {:.2f}'.format((a*12), p))
else: 
    print('COMPRA NEGADA (O valor das suas parcelas nessas condições ultrapassam 30% do seu salário atual)')