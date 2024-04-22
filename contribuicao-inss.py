salario = float(input('Qual o seu salário atual: '))
if salario <= 1751.81:
    deconto = salario * 8/100
    print('Desconto do INSS: R$ {:.6f}'.format(desconto))
elif 1751.81 < salario < 2919.73:
    desconto2 = salario * 9/100
    print('Desconto do INSS: R$ {:.6f}'.format(desconto2))
elif 2919.73 < salario < 5839.46:
    desconto3 = salario * 9/100
    print('Desconto do INSS: R$ {:.6f}'.format(desconto3))
elif salario > 5839.46:
    desconto4 = salario * 11/100
    print('Desconto do INSS: R$ {:.6f}'.format(desconto4))