#Escreva um programa que leia a velocidade de um carro se ele ultrapassar 80KM/H, mostre uma mensagem informando que o mesmo foi MULTADO. A multa vai custar 7,00R$ a cada KM acima do limite.
print('{:=^40}'.format('Analisador de Multas'))
km = int(input('Digite quantos KM/H você estava: '))
if km > 80:
    print('Você foi MULTADO, valor cobrado de multa {},00R$'.format((km-80)*7))
else: 
    print('Continue dirigindo cuidadosamente.')
