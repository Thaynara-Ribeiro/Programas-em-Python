# Desenvolva um programa que leia o comprimento de três retas, o programa deve informar ao usúario se as retas podem ou não formar um triângulo
print('{:=^40}'.format('Formando Triângulos'))
r1 = int(input('Digite o 1° comprimento de reta: '))
r2 = int(input('Digite o 2° comprimento de reta: '))
r3 = int(input('Digite o 3° comprimento de reta: '))
if r1 > (r2+r3) or r2 > (r1+r3) or r3 > (r1+r2):
    print('As retas informadas NÃO FORMAM TRIÂNGULO')
else: 
    print('As retas informadas FORMAM TRIÂNGULO')
