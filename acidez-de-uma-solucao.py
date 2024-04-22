ph = float(input('Qual o PH da solução? '))
if ph < 7:
    print('Acida')
elif ph > 7:
    print('Basica')
else: 
    print('Neutra')