#Faça um algoritmo que leia um o preço de um produto é mostre o seu novo valor. Aplicando um desconto de 5%
from time import sleep
print('{:=^40}'.format('Aplicando Desconto'))
p = int(input('Digite o valor do seu produto: '))
print('Caculando o seu novo valor...')
sleep(3)
print('Novo valor: {} R$'.format(p-(p*5/100)))
