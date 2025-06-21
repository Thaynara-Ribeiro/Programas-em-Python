# Escreva um programa que receba um valor em metros é converta para Centimetros/Milimetros
print('{:=^45}'.format('Conversor de Unidades'))
n = int(input("Digite um valor em Metros: "))
print('O valor informado equivale {} Centimetros.'.format(n*100))
print('O valor informado equivale {} Milimetros.'.format(n*1000))