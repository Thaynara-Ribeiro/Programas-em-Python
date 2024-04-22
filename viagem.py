print('{:=^40}'.format('Calculando a sua viagem'))
horas = int(input('Quantas horas foram a viagem? '))
km = int(input('Quantos KMs foram rodados? '))
distancia = (horas * km) / 12
print('A quantidade de litros gastos seria de {:.3f}L'.format(distancia))
