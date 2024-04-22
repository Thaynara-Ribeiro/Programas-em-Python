raio1 = float(input('Digite o primeiro raio do circulo: '))
raio2 = float(input('Digite o segundo raio do circulo: '))
area = 3.14 * raio1 ** 2
area2 = 3.14 * raio2 ** 2
if area == area2:
    print('Iguais')
elif area > area2:
    print('Primeiro circulo')
else:
    print('Segundo círculo')

