# Faça um programa que calcule seu Dobro, seu Triplo e sua Raiz Quadrada
print('{:=^30}'.format('Operações Aritmeticas'))
n = int(input('Informe um número para calcular o Dobro/Triplo/Raiz Quadrada: '))
print('O dobro de {} é igual= {}\nO triplo de {} é igual= {}'.format(n, n*2, n, n*3))
print('A Raiz Quadrada de {} é igual= {}'.format(n, n**(1/2)))