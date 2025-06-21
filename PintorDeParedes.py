#Faça um programa que leia a largura de uma parede em metros, calcule sua área é a qunatidade de tinta necessária
#para pinta-lá. Sabendo que cada litro de tinta pinta uma área de 2m².
print('{:=^40}'.format('Pintando sua Parede'))
l = float(input('Digite a largura da sua parede em m²: '))
a = float(input('Digite a altura da sua parede em m²: '))
print('Sabendo que cada litro de tinta pinta uma área de 2m², para pintar uma área de {:.2F}m² '.format(l*a) ,end='')
print('você precisará de {:.2f} litros de tinta'.format((l*a)/2))
