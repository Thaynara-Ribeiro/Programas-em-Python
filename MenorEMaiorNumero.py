#Faça um programa que leia três números é mostre qual é o MAIOR é qual o MENOR (Entre Eles)
print('{:=^40}'.format('Analisando Números'))
n1 = int(input('Digite o 1° Número: '))
n2 = int(input('Digite o 2° Número: '))
n3 = int(input('Digite o 3° Número: '))
if n1 > n2 and n1 > 3:
    print('O primeiro valor digitado é o MAIOR')
elif n2 > n1 and n2 > n3:
    print('O segundo valor digitado é o MAIOR')
elif n3 > n1 and n3 > n2:
    print('O terceiro valor digitado é o MAIOR')
if n1 < n2 and n1 < n3:
    print('O primeiro valor digitado é o MENOR')
elif n2 < n1 and n2 < n3:
    print('O segundo valor digitado é o MENOR')
elif n3 < n1 and n3 < n2:
    print('O terceiro valor digitado é o MENOR')
else:
    print('Os três valor são iguais.')