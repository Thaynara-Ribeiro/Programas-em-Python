print('{:=^40}'.format('Área do Trapézio'))
bmaior = int(input('Digite a Base maior: '))
bmenor = int(input('Digite a Base menor: '))
altura = int(input('Digite a altura: '))
calculo = (bmaior + bmenor) * altura / 2
print('{:.1f}'.format(calculo))