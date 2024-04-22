print('{:=^40}'.format('Calculando a área do CIRCULO'))
raio = int(input('Digite qual o raio do circulo: '))
calculo = 3.14159 * raio ** 2
conversão = calculo / 10000
print('Area = {:.4f}'.format(conversão))
