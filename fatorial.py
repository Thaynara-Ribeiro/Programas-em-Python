# Crie um programa que recebe um número e imprima o seu fatorial
# Método 5Q's para montra o algoritmo
# Analisar criticamente o problema: 
# Quais são os dados de entrada?
# (Um numero)
# O que devo fazer com esses dados?
# (Calcular o seu fatorial é exibir em tela) 
# Quais são as restrições?
# O numero deve ser positivo é inteiro
# Qual o resultado esperado? 
# E esperado ser exibido em tela o farorial do numero
# Passo a passo do Pseudocódigo?
'''input numero
if numero > 0
if numero == inteiro
fatorial = 1
loop de 1 a numero
fatorial = fatorial * numero
print(fatorial)
'''
numero = int(input('Digite um número: '))
if numero > 0:
    fatorial = 1
    for item in range(numero, 1, -1):
        fatorial = fatorial * item
print(fatorial)
