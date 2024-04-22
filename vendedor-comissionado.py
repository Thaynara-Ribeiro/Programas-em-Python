print('{:=^40}'.format('Vamos calcular o seu SALARIO'))
nome = str(input('Qual o seu nome: '))
salario = float(input('Qual o seu salario: '))
vendas = float(input('Qual o valor total das suas vendas: '))
comissão = vendas * 15/100
print('''Então você {}, possui um salario de {:.2f} é total de vendas de {:.2f}
, o valor de salario é comissão é {:.2f}'''.format(nome, salario, comissão, salario + comissão))

# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o
# total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor
# ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final
# do mês, com duas casas decimais.