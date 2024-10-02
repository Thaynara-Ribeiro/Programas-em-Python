idade = int(input('Idade: '))
if  0 < idade < 3:
    print('O individuo eh um Bebe Jovem Menor de Idade.')
elif idade > 2 and idade < 13:
    print('O individuo eh uma Crianca Jovem Menor de Idade.')
elif 12 < idade < 18:
    print('O individuo eh um Adolescente Jovem Menor de Idade.')
elif 17 < idade < 20: 
    print('O individuo eh um Jovem Maior de Idade.')
elif  19 < idade < 46:
    print('O individuo eh um Adulto Maior de Idade.')
elif 45 < idade < 60:
    print('O individuo eh um Adulto de Meia Idade Maior de Idade.')
elif  59 < idade < 76:
    print('O individuo eh um Idoso Maior de Idade.')
elif 75 < idade < 91:
    print('O individuo eh um Idoso Ansiao Maior de Idade.')
else:
    print('O individuo eh um Idoso na Velhice Extrema Maior de Idade.')