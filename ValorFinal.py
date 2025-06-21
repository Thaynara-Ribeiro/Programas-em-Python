#Elabore um programa que calcule o valor a ser pago de um produto, considerando o seu preço normal/as condições do pagamento: A vista: 10% de desconto, A vista no cartão: 5% de desconto, Parcelado até 2x cartão: Preço Normal, Parcelado Acima de 3X: 20% de Acrescimo em Juros.
print('{:=^40}'.format('Calculando o Valor Final'))
p = float(input('Digite o valor do produto: '))
print('Escolha uma forma de pagamento: A vista, A vista cartão, Parcelado 2x, Parcelado acima de 3x')
f = str(input('Digite qual sua forma de pagamento: ')).upper()
if f == 'A VISTA':
    print('O valor do produto aplicado desconto de 10% = {:.2f}R$'.format(p - p*(10/100)))
elif f == 'A VISTA CARTÃO':
    print('O valor do produto aplicado desconto de 5% = {:.2f}R$'.format(p - p*(5/100)))
elif f == 'PARCELADO 2X':
    print('O valor do produto parcelado em 2X permanece o mesmo = {}'.format(p))
elif f == 'PARCELADO ACIMA DE 3X':
    print('O valor com acrescimo de 20% de juros = {:.2f}'.format(p*(20/100)+p))
else: 
    print('Digite uma OPÇÃO VALIDA')