#Desenvolva um programa que leia o peso é a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: Abaixo de 18.5 (Abaixo do Peso), Entre 18.5/25 (Peso Ideal), Entre 25/30 (Sobrepeso), Entre 30/40 (Obesidade), Acima de 40 (Obesidade Morbida)
print('{:=^40}'.format('Calculando seu IMC'))
p = float(input('Digite seu Peso em KGs: '))
a = float(input('Digite sua Altura em Metros: '))
imc = p / (a*a)
if imc < 18.5:
    print('ABAIXO DO PESO IDEAL')
elif imc > 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc > 25 and imc < 30:
    print('SOBREPESO')
elif imc > 30 and imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')
print('O seu IMC é {:.2f}'.format(imc))