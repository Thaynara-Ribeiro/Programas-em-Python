print('{:=^40}'.format('Calculando gastos'))
conta = float(input('Qual o valor total gasto? '))
desconto = conta * 10/100
resultado = conta + desconto
print('O valor total da sua refeição seria {:.2f}'.format(resultado))

#  Faça um programa que leia um valor representando o gasto realizado por
# um cliente do restaurante COMABEM e imprima o valor total a ser pago, considerando os
# 10% do garçom.