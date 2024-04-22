salario = float(input('Digite o seu salario: '))
if salario >= 280: 
    aumento = salario * 20/100
    print('{:.2f}'.format(salario + aumento))
elif 280 < salario < 701:
    aumento2  = salario * 15/100
    print('{:.2f}'.format(salario + aumento2))
elif 700 < salario < 1501:
    aumento3 = salario * 10/100
    print('{:.2f}'.format(salario + aumento3))
else: 
    aumento4 = salario * 5/100
    print('{:.2f}'.format(salario + auamento4))