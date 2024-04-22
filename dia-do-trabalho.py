salario = float(input('Informe o seu salário atual: '))
if salario > 500:
    aumento = salario * 10/100
    print('{:.2f}'.format(salario + aumento))
elif 299 < salario < 501:
    aumento2 = salario * 7/100
    print('{:.2f}'.format(salario + aumento2))
else:
    aumento3 =  salario3 * 5/100
    print('{:.2f}'.format(salario + aumento3))