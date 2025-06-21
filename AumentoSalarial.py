print('{:=^40}'.format('Calculando Seu Aumento'))
s = int(input('Digite seu Salário Atual: '))
if s <= 1250:
    print('O seu novo salário: {}'.format(s*(15/100)+s))
else:
    print('O seu novo salário: {}'.format(s*(10/100)+s))