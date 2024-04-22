print('{:=^40}'.format('Validação de dados'))
sexo = str(input('Digite o seu sexo: [F/M] ')).strip().upper()
while sexo not in 'FfMm':
    print('Sexo invalido, Tente novamente')
    sexo = str(input('Digite F/M para informar o seu sexo: ')).strip().upper()
if sexo == 'F':
        print('Sexo Feminino, registrado com sucesso')
elif sexo == 'M':
        print('Sexo Masculino, registrado com sucesso')
