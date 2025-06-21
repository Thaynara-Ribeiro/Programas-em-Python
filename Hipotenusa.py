#Faça um programa que leia o comprimento do cateto Oposto/Adjacente de um triângulo retângulo. Calcule sua Hipotenusa
import math
print('{:=^40}'.format('Calculando a Hipotenusa'))
o = int(input('Digite o comprimento do Cateto Oposto: '))
a = int(input('Digite o comprimento do Cateto Adjacente: '))
r = (o**2) + (a**2)
print('A hipotenusa tendo como base nos catetos Oposto/Adjacente é {}'.format(math.sqrt(r)))