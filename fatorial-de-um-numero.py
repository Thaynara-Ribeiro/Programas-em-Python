'''
***Problema***
Crie um programa calcule o fatorial de qualquer número informado pelo usuário?
Utilizando o Metodo 5Qs
Qual os dados de entrada?
Oque fazer com esses dados?
Qual as restrições do programa?
Qual o resultado esperado?
Qual a sequência de passo a passo em Pseudocódigo?
'''
'''Solução'''
numero = int(input('Digite um numero: '))
fatorial = 1
if numero > 0:
    for c in range(numero, 1, -1):
        fatorial = fatorial * c
print('O fatorial do numero {} é {}'.format(numero,fatorial))