'''
Execute um programa que calcule a partir da altura e o valor do raio
calcule a área de um cilindro.
'''
print('{:=^}'.format('Volume é Area do CILINDRO'))
altura = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro: ')) 
volume  = 3.14 * raio ** 2 * altura
area = (2 * 3.14 * raio ** 2) + (2 * 3.14 * raio *altura)
print('''
{:.2f}
{:.2f}
'''.format(volume, area))
