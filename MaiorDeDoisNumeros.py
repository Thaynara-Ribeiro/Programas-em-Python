#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O primeiro número é o MAIOR, o segundo número é o MAIOR ou NÃO EXISTE MAIOR, ambos os números são iguais.
print('{:=^40}'.format('Comparando Números'))
n1 = int(input('Digito o 1° Valor: '))
n2 = int(input('Digite o 2° Valor: '))
if n1 > n2:
    print('O Primeiro Valor é o MAIOR')
elif n2 > n1:
    print('O Segundo Valor é o MAIOR')
else: 
    print('NÃO EXISTE NÚMERO MAIOR, ambos são IGUAIS')