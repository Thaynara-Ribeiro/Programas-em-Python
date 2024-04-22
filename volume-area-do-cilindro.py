print('{:=^}'.format('Volume é Area do CILINDRO'))
altura = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro: ')) 
volume  = 3.14 * raio ** 2 * altura
area = (2 * 3.14 * raio ** 2) + (2 * 3.14 * raio *altura)
print('''
{:.2f}
{:.2f}
'''.format(volume, area))
