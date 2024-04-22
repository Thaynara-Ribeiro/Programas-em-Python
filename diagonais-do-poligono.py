print('{:=^40}'.format('Diagonais de um POLIGONO'))
lado = int(input('Quantos lados possui o poligono: '))
resultado = lado * (lado - 3) / 2
print('{:.0f}'.format(resultado))