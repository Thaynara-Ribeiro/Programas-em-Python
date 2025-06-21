 #Faça um programa que converta uma temperatura de Celsis para Fahrenheint
print('{:=^40}'.format('Conversor de Temperaturas'))
t = int(input('Digite sua temperatura de Graus Celsios: '))
print('A sua temperatura de {}°C convertida para {:.1f}°F'.format(t, (t*1.8)+32))