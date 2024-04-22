salario = float(input('Digite o seu salario atual: '))
bonus = salario * 75/100
if bonus < 2000:
    print('ARGENTINA')
elif 2000 < bonus < 3001:
    print('ESPANHA')
else:
    print('ALEMANHA')