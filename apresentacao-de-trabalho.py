r1 = str(input('Trabalho aborda Interface Gráfica? (0 - Nao 1 - Sim)'))
r2 = str(input('Trabalho aborda Inteligencia Artificial? (0 - Nao 1 - Sim)'))
r3 = str(input('Trabalho aborda Encapsulamento? (0 - Nao 1 - Sim)'))
r4 = str(input('Trabalho aborda Indentacao? (0 - Nao 1 - Sim)'))
r5 = str(input('Trabalho aborda Structs? (0 - Nao 1 - Sim)'))
if r1 == '1' and r3 == '1' and r4 == '1' and r5 == '1':
    print('Seu trabalho sera avaliado.')
elif r2 == '1' and r3 == '1' and r4 == '1' and r5 == '1':
    print('Seu trabalho sera avaliado.')
else:
    print('Seu trabalho nao sera avaliado, nota 0.')
